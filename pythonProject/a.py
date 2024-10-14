import sys
from PyQt5.QtWidgets import QApplication
from registration import RegistrationApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationApp()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__() #Initialize the main window like the previous one
        # window = QMainwIndow()
        self.title = "PyQt Button"
        self.x=200 #or left
        self.y=200 #or top
        self.width=300
        self.height=300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        # Create Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(40, 20)
        self.textbox.resize(220, 40)
        self.textbox.setText("Set this text value")

        #1st text
        self.textboxbl = QLabel("Hello World!", self)
        self.textboxbl.move(30, 25)

        #2nd text
        self.textboxbl2 = QLabel("This program is written in Pycharm", self)
        self.textboxbl2.move(30, 55)

        self.show()

        self.button2 = QPushButton('Register now!', self)
        self.button2.setToolTip("Click the button to register!")
        self.button2.move(100, 150)
        self.show()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        Main = App()
        sys.exit(app.exec_())

Task
Create an Object-Oriented GUI Application for a simple Account Registration System with the following required information:
first name, last name, username, password, email address, contact number.
Requirements:
• The GUI must be centered on your screen.
• The GUI Components should be organized according to the order of information required using Absolute Positioning.
• The position of the components should be automatically computed based on the top component.
• All the text fields should be accompanied with their corresponding label on the left side while the text field is on the
right side.
• There should a program title other than the Window Title.
• There should be a submit button and clear button at the bottom (submit button on the left, clear button on the right).
• The program should be launched on main.py while the GUI Codes should be on a separate file called
registration.py
