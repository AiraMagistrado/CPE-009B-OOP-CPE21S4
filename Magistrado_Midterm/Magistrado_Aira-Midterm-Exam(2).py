import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.button = QPushButton('Click to change color', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100, 100)  # button.move(x, y)
        self.button.clicked.connect(self.change_background)
        self.show()

    def change_background(self):
        self.setStyleSheet("background-color: yellow;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())
