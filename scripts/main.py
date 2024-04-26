import sys
import os
sys.path.append(os.path.abspath('src'))

from src import registration, search_chtas
from src import db
from PyQt6.QtWidgets import QApplication

def start_app():
    app = QApplication([])
    database = db.DataBase()
    if database.check_db() == False:
        windows = registration.Registration_windows()
        windows.show()
    else:
        window = search_chtas.Search_window()
        window.show()
    sys.exit(app.exec())