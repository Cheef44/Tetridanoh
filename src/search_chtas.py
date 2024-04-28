from PyQt6.QtWidgets import QWidget
import search_programm_interface
from PyQt6 import QtWidgets
import db
import socket
import json

class Search_window(QWidget, search_programm_interface.Ui_MainWindow):
    def __init__(self, server:socket.socket):
        super().__init__()
        self.server = server
        
        self.setFixedSize(538, 463)
        self.setupUi(self)
        name = db.DataBase().retrieve_data()[0][0][0]
        self.nick_name.setText(name)
        self.tabWidget.currentChanged.connect(self.All_chats)
    
    def All_chats(self, index):
        if index == 1:
            values = [self.all_list.item(item_index).text() for item_index in range(self.all_list.count())]
            keys = []
            self.server.send((json.dumps(["(ALLCHATS)"]).encode('utf-8')))
            server_data = self.server.recv(1024)
            server_data = json.loads(server_data)
            if server_data:
                for i in server_data:
                    keys.append(i[0])
                    self.items = {k:v for k,v in zip(keys,values)}
                    if not i[0] in self.items.keys():
                        self.all_list.addItem(i[1])