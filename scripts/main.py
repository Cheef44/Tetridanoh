import sys
import os
sys.path.append(os.path.abspath('src'))

from src import registration, search_chtas
from src import db
from PyQt6.QtWidgets import QApplication
import socket
import json
from threading import Thread

def start_app():
    client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('DESKTOP-96M1JI1', 1488))
    app = QApplication([])
    database = db.DataBase()
    if database.check_db() == False:
        windows = registration.Registration_windows(client)
        windows.show()
    else:
        window = search_chtas.Search_window()
        window.show()
    sys.exit(app.exec())