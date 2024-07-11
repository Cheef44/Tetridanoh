from PyQt6.QtWidgets import QWidget, QListWidgetItem, QApplication, QMessageBox
import messages_programm_interface
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
import db
import socket
import json
from PyQt6.QtGui import QCloseEvent
import datetime
import logging
import db
import socket
import json
import logging
logging.basicConfig(level=logging.DEBUG)

#Класс приема сообщений
class GetMessage(QThread):
    data_received = pyqtSignal(list)

    def __init__(self, server):
        super().__init__()
        self.server = server
        self._running = True
        
    def run(self):
        try:
            while self._running:
                server_data = self.server.recv(1024)
                server_data = json.loads(server_data)
                if server_data[0] == '(MESSAGE)':
                    message_text = server_data[1]
                    self.data_received.emit(message_text)
        except Exception as e:
            logging.error(f"Ошибка в процессе worker: {e}")
    def stop(self):
        self._running = False
        
#Класс менеджера чатов       
class ChatMenager(QThread):
    data = pyqtSignal(list)
    def __init__(self, server:socket.socket, index):
        super().__init__()
        self.server = server
        self.index = index
        self._running = True
        
    def load_all_chats(self):
        self.server.send((json.dumps(["(ALLCHATS)", db.DataBase().retrieve_data()[-1][0][0]]).encode('utf-8')))
        server_data = self.server.recv(1024)
        server_data = json.loads(server_data)
        #logging.debug(f'server_data_a: {server_data}')
        if server_data[0] == "(ALLCHATS)":
            id = server_data[1][-1][0]
            #logging.debug(f'id_user:{id}')
            self.data.emit([server_data[1:][0], id])
        elif server_data[0] == '(ALLFREANDS)':
            self.load_freands_chats()
    
    def load_freands_chats(self):
        email = ''.join(db.DataBase.retrieve_data(False)[-1][0])
        user_data = ['(ALLFREANDS)', email]
        self.server.sendall(json.dumps(user_data).encode('utf-8'))
        server_data = self.server.recv(1024)
        server_data = json.loads(server_data)
        #logging.debug(f'server_data_f: {server_data}')
        if server_data[0] == '(ALLFREANDS)':
            self.data.emit(server_data[1:][0])
        elif server_data[0] == "(ALLCHATS)":
            self.load_all_chats()
    
    def run(self):
        if self.index == 0:
            self.load_freands_chats()
        else:
            self.load_all_chats()
    
    def stop(self):
        self._running = False

#Класс добавления пользователей в друзья
class AddChat(QThread):
    data = pyqtSignal(bool)
    
    def __init__(self, server:socket.socket, email, chat_id):
        super().__init__()
        self.server = server
        self.email = email
        self.chat_id = chat_id
    
    def run(self):
        user_data = ['(ADDCHAT)', self.email, self.chat_id]
        self.server.sendall(json.dumps(user_data).encode('utf-8'))
        server_data = self.server.recv(1024)
        server_data = json.loads(server_data)
        #logging.debug(f'server_data_add: {server_data}')
        if server_data[0] == '(ADDCHAT)':
            self.data.emit(server_data[1])
            
#Основной класс окна
class Message_windows(QWidget, messages_programm_interface.Ui_MainWindow):
    def __init__(self, server: socket.socket):
        super().__init__()
        self.all_chats = {}
        self.keys = []
        self.user_db = db.DataBase()
        self.email = self.user_db.retrieve_data()[-1][0][0]
        self.server = server
        self.chat_id = 1
        self.open_mess = False
        self.setupUi(self)
        self.get_message = GetMessage(self.server)
        self.tabWidget.setCurrentIndex(0)
        self.nickname.setText('')
        self.text_messages.installEventFilter(self)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.all_list.itemClicked.connect(self.get_chat_data)
        self.search_chats.textChanged.connect(self.search)
        self.freand_list.itemClicked.connect(self.open_message)
        self.tab_changed(self.tabWidget.currentIndex())
          
    def tab_changed(self, index):
        #logging.debug(f'tab_index: {index}')
        self.chat_menager = ChatMenager(self.server, index)
        if index == 0:
            if self.open_mess == False:
                self.chat_menager.data.connect(self.update_freands_chtas)
        else:
            if self.open_mess == False:
                self.chat_menager.data.connect(self.update_all_chats)
        self.chat_menager.start()
        
    @pyqtSlot(list)
    def update_all_chats(self, data):
        #logging.debug(f'all_chats: {data}')
        self.keys = []
        self.all_list.clear()
        for item in data[0]:
            if item[0] != data[1]:
                self.keys.append(item[0])
                self.all_list.addItem(item[1])
                values = [self.all_list.item(index).text() for index in range(self.all_list.count())]
                self.all_chats = {k:v for k, v in zip(self.keys, values)}
    
    def get_chat_data(self, item):
        if self.open_mess == False:
            self.add_index = self.all_list.row(item)
            if self.all_chats:
                add_chat = QMessageBox.question(None, "Добавление пользователя", f"Хотите ли вы добавить пользователя {self.all_chats[self.keys[self.add_index]]} с id: {self.keys[self.add_index]} в дружеские чаты?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if add_chat == QMessageBox.StandardButton.Yes:
                    chat_id = self.keys[self.add_index]
                    email = ''.join(db.DataBase.retrieve_data(False)[-1][0])
                    self.add_chat = AddChat(self.server, email, chat_id)
                    self.add_chat.data.connect(self.check_add_chat)
        self.add_chat.start()
    @pyqtSlot(bool)
    def check_add_chat(self, check_add):
        logging.debug(f'check_add: {check_add}')
        if check_add == True:
            QMessageBox.information(None, "Добавление пользователя", f"Пользователь {self.all_chats[self.keys[self.add_index]]} был добавлен в дружеские чаты")
        else:
            QMessageBox.information(None, "Добавление пользователя", f"Пользователь {self.all_chats[self.keys[self.add_index]]} уже есть у вас в друзьях")
    
    @pyqtSlot(list)
    def update_freands_chtas(self, data):
        #logging.debug(f'freand_chats: {data}')
        self.freand_keys = []
        self.freand_list.clear()
        for item in data:
            self.freand_list.addItem(item[0])
            self.freand_keys.append(item[1])
            values = [self.freand_list.item(item_index).text() for item_index in range(self.freand_list.count())]
            self.freand_items = {k:v for k,v in zip(self.freand_keys,values)}
                 
    def open_message(self, item):
        self.chat_menager.wait(1)
        self.open_mess = True
        index = self.freand_list.row(item)
        self.nickname.setText(self.freand_items[self.freand_keys[index]])
        self.chat_id = self.freand_keys[index]
        self.get_message.data_received.connect(self.handle_data_received)
        self.get_message.start()
        
    @pyqtSlot(list)    
    def handle_data_received(self, data):
        item = QListWidgetItem(data[0])
        if data[1] == 2:
            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
        else:
            item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.messages.addItem(item)

    def eventFilter(self, obj, event):
        if obj is self.text_messages and event.type() == QtCore.QEvent.Type.KeyPress:
            key = event.key()
            modifiers = QApplication.keyboardModifiers()
            if (key == Qt.Key.Key_Return or key == Qt.Key.Key_Enter) and not (modifiers & Qt.KeyboardModifier.ShiftModifier):
                text = self.text_messages.toPlainText()
                self.send_message(text)
                return True
            if key == Qt.Key.Key_Escape:
                self.nickname.setText('')
        return super().eventFilter(obj, event)
    
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_Escape and self.open_mess:
           self.nickname.setText('')
           self.open_mess = False
           self.messages.clear()
           self.get_message.stop()
           self.get_message.wait(1)
    
    def send_message(self, text):
        item = QListWidgetItem(f'{text}\n{datetime.datetime.today().time().hour}:{datetime.datetime.today().time().minute} {datetime.datetime.today().date()}')
        item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        history_messages = [item.text(), Qt.AlignmentFlag.AlignRight]
        self.server.send(json.dumps(['(HISTORYMESSAGE)', self.chat_id, self.email, history_messages]).encode('utf-8'))
        self.messages.addItem(item)
        self.text_messages.clear()
    
    def closeEvent(self, event: QCloseEvent):
        self.get_message.stop()
        self.get_message.wait(1)
        self.chat_menager.wait(1)
        #logging.debug('Закрытие окна')
        #logging.debug("Поток завершен.")
        event.accept()