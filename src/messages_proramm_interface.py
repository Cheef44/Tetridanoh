# Form implementation generated from reading ui file 'ui\messages-proramm_interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 463)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nickname = QtWidgets.QLabel(parent=self.centralwidget)
        self.nickname.setGeometry(QtCore.QRect(10, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nickname.setFont(font)
        self.nickname.setObjectName("nickname")
        self.text_messages = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_messages.setGeometry(QtCore.QRect(20, 420, 491, 31))
        self.text_messages.setObjectName("text_messages")
        self.messages = QtWidgets.QListView(parent=self.centralwidget)
        self.messages.setGeometry(QtCore.QRect(20, 50, 491, 361))
        self.messages.setObjectName("messages")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nickname.setText(_translate("MainWindow", "NickName"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())