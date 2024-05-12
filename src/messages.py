from PyQt6.QtWidgets import QWidget, QMessageBox
import messages_proramm_interface
from PyQt6 import QtWidgets
import db
import socket
import json
import time

class Message_windows(QWidget, messages_proramm_interface.Ui_MainWindow):
    def __init__(self, server:socket.socket, nick_name):
        super().__init__()
        self.setupUi(self)
        self.nickname.setText(nick_name)