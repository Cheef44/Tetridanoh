import sys
import os
sys.path.append(os.path.abspath('../src'))

from PyQt6.QtWidgets import QWidget, QMessageBox
import search_programm_interface
from PyQt6 import QtWidgets
import db
import socket
import json
import time
from plyer import notification
import src.messages as messages

class Search_window(QWidget, search_programm_interface.Ui_MainWindow):
    def __init__(self, server:socket.socket):
        super().__init__()
        self.server = server
        self.puk = False
        self.setFixedSize(538, 463)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        name = db.DataBase().retrieve_data()[0][0][0]
        self.nick_name.setText(name)
        if self.tabWidget.currentIndex() == 0:
            self.freands_chats(0)
        self.tabWidget.currentChanged.connect(self.freands_chats)
        self.tabWidget.currentChanged.connect(self.All_chats)
        self.all_list.itemClicked.connect(self.add_chat)
        self.search_chats.textChanged.connect(self.search)
        self.freand_list.itemClicked.connect(self.open_message)
    
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
            self.server.send((json.dumps(["(RETRIVEDATA)", db.DataBase().retrieve_data()[-1][0][0]]).encode('utf-8')))
            id = self.server.recv(1024)
            id = json.loads(id)
            if server_data:
                for i in server_data:
                    if i[0] != id[0][0]:
                        self.keys.append(i[0])
                        self.all_items = {k:v for k,v in zip(self.keys,values)}
                        if not i[0] in self.all_items.keys():
                            self.all_list.addItem(i[1])
            self.tabWidget.setCurrentIndex(1)

    def add_chat(self, item):
        index = self.all_list.row(item)
        if self.all_items:
            add_chat = QMessageBox.question(None, "Добавление пользователя", f"Хотите ли вы добавить пользователя {self.all_items[self.keys[index]]} с id: {self.keys[index]} в дружеские чаты?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if add_chat == QMessageBox.StandardButton.Yes:
                chat_id = self.keys[index]
                email = ''.join(db.DataBase.retrieve_data(False)[-1][0])
                user_data = ['(ADDCHAT)', email, chat_id]
                self.server.sendall(json.dumps(user_data).encode('utf-8'))
                server_data = self.server.recv(1024)
                server_data = json.loads(server_data)
                if server_data == True:
                    QMessageBox.information(None, "Добавление пользователя", f"Пользователь {self.all_items[self.keys[index]]} был добавлен в дружеские чаты")
                else:
                    QMessageBox.information(None, "Добавление пользователя", f"Пользователь {self.all_items[self.keys[index]]} уже есть у вас в друзьях")
    
    def freands_chats(self, index):
        if index == 0:
            email = ''.join(db.DataBase.retrieve_data(False)[-1][0])
            user_data = ['(ALLFREANDS)', email]
            self.server.sendall(json.dumps(user_data).encode('utf-8'))
            values = [self.freand_list.item(item_index).text() for item_index in range(self.freand_list.count())]
            self.freand_keys = []
            if user_data:
                server_data = self.server.recv(1024)
                server_data = json.loads(server_data)
                if server_data:
                    for i in server_data:
                        self.freand_keys.append(i[1])
                        self.freand_items = {k:v for k,v in zip(self.freand_keys,values)}
                        if not i[1] in self.freand_items.keys():
                            self.freand_list.addItem(i[0])
                else:
                    self.freand_list.clear()
    
    def search(self, text):
        if self.tabWidget.currentIndex() == 1:
            all_chats = [i[1] for i in self.all_items.items()]
            self.all_list.clear()
            for chat in all_chats:
                if text in chat:
                    self.all_list.addItem(chat)
        if self.tabWidget.currentIndex() == 0:
            freand_chats = [i[1] for i in self.freand_items.items()]
            self.freand_list.clear()
            for freand_chat in freand_chats:
                if text in freand_chat:
                    self.freand_list.addItem(freand_chat)
    
    def open_message(self, item):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        index = self.freand_list.row(item)
        nick_name = self.freand_items[self.freand_keys[index]]
        self.window = messages.Message_windows(self.server, nick_name)
        self.window.show()