# Form implementation generated from reading ui file 'ui\registration-programm_interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 50, 311, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.registration_input = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.registration_input.setContentsMargins(0, 0, 0, 0)
        self.registration_input.setSpacing(0)
        self.registration_input.setObjectName("registration_input")
        self.nickname = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nickname.sizePolicy().hasHeightForWidth())
        self.nickname.setSizePolicy(sizePolicy)
        self.nickname.setStyleSheet("margin-bottom: 30px;")
        self.nickname.setObjectName("nickname")
        self.registration_input.addWidget(self.nickname)
        self.email = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)
        self.email.setStyleSheet("margin-bottom: 30px;")
        self.email.setObjectName("email")
        self.registration_input.addWidget(self.email)
        self.password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet("margin-bottom: 30px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.registration_input.addWidget(self.password)
        self.password_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_2.sizePolicy().hasHeightForWidth())
        self.password_2.setSizePolicy(sizePolicy)
        self.password_2.setStyleSheet("margin-bottom: 30px;")
        self.password_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_2.setObjectName("password_2")
        self.registration_input.addWidget(self.password_2)
        self.button = QtWidgets.QHBoxLayout()
        self.button.setSpacing(0)
        self.button.setObjectName("button")
        self.Login = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy)
        self.Login.setObjectName("Login")
        self.button.addWidget(self.Login)
        self.Registration = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Registration.sizePolicy().hasHeightForWidth())
        self.Registration.setSizePolicy(sizePolicy)
        self.Registration.setObjectName("Registration")
        self.button.addWidget(self.Registration)
        self.registration_input.addLayout(self.button)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tetridanoh"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.Registration.setText(_translate("MainWindow", "Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
