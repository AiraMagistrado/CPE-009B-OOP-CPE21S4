import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__() #initializes the main window like in previous one
        #window = QMainWindow()
        self.title = "PyQt Line Edit"
        self.x=200 #or left
        self.y=200 #or top
        self.width=300
        self.height=300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

    #Create Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(40,20)
        self.textbox.resize(220,40)
        self.textbox.setText("Set this text value")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())