import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton

class RegistrationApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)

        self.label_first_name = QLabel("Enter your full name:", self)
        self.label_first_name.move(30, 50)
        self.textbox_first_name = QLineEdit(self)
        self.textbox_first_name.move(150, 50)
        self.textbox_first_name.resize(200, 30)

        self.submit_button = QPushButton('Click to display your Fullname', self)
        self.submit_button.setToolTip("Click to display")
        self.submit_button.move(30, 90)
        self.submit_button.clicked.connect(self.submit)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def submit(self):
        first_name = self.textbox_first_name.text()

        print(f"First Name: {first_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationApp()
    sys.exit(app.exec_())