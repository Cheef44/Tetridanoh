# Form implementation generated from reading ui file 'messages-proramm_interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 782)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nickname = QtWidgets.QLabel(parent=self.centralwidget)
        self.nickname.setGeometry(QtCore.QRect(570, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nickname.setFont(font)
        self.nickname.setObjectName("nickname")
        self.text_messages = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_messages.setGeometry(QtCore.QRect(570, 740, 491, 31))
        self.text_messages.setObjectName("text_messages")
        self.messages = QtWidgets.QListWidget(parent=self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(570, 50, 491, 671))
        self.messages.setObjectName("messages")
        self.search_chats = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.search_chats.setGeometry(QtCore.QRect(20, 20, 541, 31))
        self.search_chats.setObjectName("search_chats")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 541, 711))
        self.tabWidget.setObjectName("tabWidget")
        self.freand_chats = QtWidgets.QWidget()
        self.freand_chats.setObjectName("freand_chats")
        self.freand_list = QtWidgets.QListWidget(parent=self.freand_chats)
        self.freand_list.setGeometry(QtCore.QRect(-10, -10, 551, 701))
        self.freand_list.setObjectName("freand_list")
        self.tabWidget.addTab(self.freand_chats, "")
        self.all_chats = QtWidgets.QWidget()
        self.all_chats.setObjectName("all_chats")
        self.all_list = QtWidgets.QListWidget(parent=self.all_chats)
        self.all_list.setGeometry(QtCore.QRect(-5, -9, 551, 701))
        self.all_list.setObjectName("all_list")
        self.tabWidget.addTab(self.all_chats, "")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nickname.setText(_translate("MainWindow", "NickName"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.freand_chats), _translate("MainWindow", "Freands"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all_chats), _translate("MainWindow", "Other"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
