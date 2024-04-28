import sys
import os
sys.path.append(os.path.abspath('src'))

from src import registration, search_chtas, db
from src import db
from PyQt6.QtWidgets import QApplication
import socket
import json

class Main():
    def __init__(self) -> None:
        pass
        
    def update(self, client:socket.socket):
        name,password,email = db.DataBase.retrieve_data(False)
        name,password,email = name[0][0], password[0][0], email[0][0]
        user_data = ['(REGISTRETION&UPDATE)', name, password, email]
        client.sendall(json.dumps(user_data).encode('utf-8'))

    def start_app(self):
        self.client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('DESKTOP-96M1JI1', 1488))
        app = QApplication([])
        database = db.DataBase()
        if database.check_db() == False:
            windows = registration.Registration_windows(self.client)
            windows.show()
        else:
            self.update(self.client)
            window = search_chtas.Search_window(self.client)
            window.show()
        sys.exit(app.exec())