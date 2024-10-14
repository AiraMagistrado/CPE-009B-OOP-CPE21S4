from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class RegistrationApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Account Registration Form"
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.center()

        self.program_title = QLabel("Account Registration", self)
        self.program_title.setAlignment(Qt.AlignCenter)
        self.program_title.setGeometry(0, 10, self.width, 30)

        self.label_first_name = QLabel("First Name:", self)
        self.label_first_name.move(30, 50)
        self.textbox_first_name = QLineEdit(self)
        self.textbox_first_name.move(150, 50)
        self.textbox_first_name.resize(200, 30)

        self.label_last_name = QLabel("Last Name:", self)
        self.label_last_name.move(30, 90)
        self.textbox_last_name = QLineEdit(self)
        self.textbox_last_name.move(150, 90)
        self.textbox_last_name.resize(200, 30)

        self.label_username = QLabel("Username:", self)
        self.label_username.move(30, 130)
        self.textbox_username = QLineEdit(self)
        self.textbox_username.move(150, 130)
        self.textbox_username.resize(200, 30)

        self.label_password = QLabel("Password:", self)
        self.label_password.move(30, 170)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.move(150, 170)
        self.textbox_password.resize(200, 30)
        self.textbox_password.setEchoMode(QLineEdit.Password)

        self.label_email = QLabel("Email Address:", self)
        self.label_email.move(30, 210)
        self.textbox_email = QLineEdit(self)
        self.textbox_email.move(150, 210)
        self.textbox_email.resize(200, 30)

        self.label_contact = QLabel("Contact Number:", self)
        self.label_contact.move(30, 250)
        self.textbox_contact = QLineEdit(self)
        self.textbox_contact.move(150, 250)
        self.textbox_contact.resize(200, 30)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setToolTip("Click to submit")
        self.submit_button.move(100, 300)
        self.submit_button.clicked.connect(self.submit)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setToolTip("Click to clear")
        self.clear_button.move(200, 300)
        self.clear_button.clicked.connect(self.clear)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def submit(self):
        first_name = self.textbox_first_name.text()
        last_name = self.textbox_last_name.text()
        username = self.textbox_username.text()
        password = self.textbox_password.text()
        email = self.textbox_email.text()
        contact = self.textbox_contact.text()

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Email: {email}")
        print(f"Contact: {contact}")

    def clear(self):
            self.textbox_first_name.clear()
            self.textbox_last_name.clear()
            self.textbox_username.clear()
            self.textbox_password.clear()
            self.textbox_email.clear()
            self.textbox_contact.clear()

