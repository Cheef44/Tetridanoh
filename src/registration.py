import sys
import os
sys.path.append(os.path.abspath('../src'))

from PyQt6.QtWidgets import QWidget, QApplication
import registration_programm_interface
import db
import src.messages as messages
import socket
import json

class Registration_windows(QWidget, registration_programm_interface.Ui_MainWindow):
    def __init__(self, client:socket.socket):
        super().__init__()
        self.client = client
        self.setupUi(self)
        self.setFixedSize(500, 400)
        self.Registration.clicked.connect(
            lambda: self.registration(name=self.nickname.text(), email=self.email.text(), password=self.password.text(), password_2=self.password_2.text())
            )
        
    def registration(self, name, email, password, password_2):
        if password == password_2:
            user = db.DataBase(password, name, email)
            user_data = ['(REGISTRETION&UPDATE)', name, password, email]
            self.client.send(json.dumps(user_data).encode('utf-8'))
            user.create_db()
            self.open_search_chats()
    
    def open_search_chats(self):
        self.close()
        self.window = messages.Message_windows(self.client)
        self.window.show()