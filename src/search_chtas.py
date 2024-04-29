from PyQt6.QtWidgets import QWidget, QMessageBox
import search_programm_interface
from PyQt6 import QtWidgets
import db
import socket
import json
import time
from plyer import notification

class Search_window(QWidget, search_programm_interface.Ui_MainWindow):
    def __init__(self, server:socket.socket):
        super().__init__()
        self.server = server
        self.puk = False
        
        self.setFixedSize(538, 463)
        self.setupUi(self)
        name = db.DataBase().retrieve_data()[0][0][0]
        self.nick_name.setText(name)
        self.tabWidget.currentChanged.connect(self.All_chats)
        self.all_list.itemClicked.connect(self.add_chat)
    
    def All_chats(self, index):
        if self.puk == False:
            self.tabWidget.setCurrentIndex(0)
            self.puk = True
        if index == 1:
            values = [self.all_list.item(item_index).text() for item_index in range(self.all_list.count())]
            self.keys = []
            self.server.send((json.dumps(["(ALLCHATS)"]).encode('utf-8')))
            server_data = self.server.recv(1024)
            server_data = json.loads(server_data)
            if server_data:
                for i in server_data:
                    if i[1] != self.nick_name.text():
                        self.keys.append(i[0])
                        self.items = {k:v for k,v in zip(self.keys,values)}
                        if not i[0] in self.items.keys():
                            self.all_list.addItem(i[1])
            self.tabWidget.setCurrentIndex(1)

    def add_chat(self, item):
        index = self.all_list.row(item)
        if self.items:
            add_chat = QMessageBox.question(None, "Добавление пользователя", f"Хотите ли вы добавить пользователя: {self.items[self.keys[index]]} в дружеские чаты?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if add_chat == QMessageBox.StandardButton.Yes:
                chat_id = self.keys[index]
                email = ''.join(db.DataBase.retrieve_data(False)[-1][0])
                user_data = ['(ADDCHAT)', email, chat_id]
                self.server.sendall(json.dumps(user_data).encode('utf-8'))
                server_data = self.server.recv(1024)
                server_data = json.loads(server_data)
                if server_data == True:
                    QMessageBox.information(None, "Добавление пользователя", f"Пользователь {self.items[self.keys[index]]} был добавлен в дружеские чаты")
                else:
                    QMessageBox.information(None, "Добавление пользователя", f"Пользователь {self.items[self.keys[index]]} уже есть у вас в друзьях")