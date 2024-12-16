import sys
import math
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout, \
    QVBoxLayout, QAction, QFileDialog, QMenuBar
from PyQt5.QtGui import QIcon


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('python.ico'))
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.createMenu()
        self.createButtons()
        self.createLayout()

        self.show()

    def createMenu(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('File')
        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveToFile)
        fileMenu.addAction(saveAction)

        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.loadFromFile)
        fileMenu.addAction(openAction)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        clearAction = QAction('Clear', self)
        clearAction.setShortcut('Ctrl+C')
        clearAction.triggered.connect(self.clear)
        menuBar.addAction(clearAction)

    def createButtons(self):
        self.display = QLineEdit(self)

        self.buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', 'sin',
            '0', '.', '=', '+', 'cos'
        ]

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.display, 0, 0, 1, 5)

        positions = [(i, j) for i in range(1, 5) for j in range(5)]
        for position, button_text in zip(positions, self.buttons):
            button = QPushButton(button_text)
            button.clicked.connect(self.onButtonClick)
            self.gridLayout.addWidget(button, *position)

    def createLayout(self):
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(self.gridLayout)
        self.centralWidget.setLayout(mainLayout)

    def onButtonClick(self):
        sender = self.sender().text()

        if sender == 'C':
            self.clear()
        elif sender == '=':
            self.calculate()
        elif sender in ['sin', 'cos', '√']:
            self.calculateSpecial(sender)
        else:
            self.display.setText(self.display.text() + sender)

    def calculate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")

    def calculateSpecial(self, operation):
        try:
            value = float(self.display.text())
            if operation == 'sin':
                result = math.sin(math.radians(value))
            elif operation == 'cos':
                result = math.cos(math.radians(value))
            elif operation == '√':
                result = math.sqrt(value)
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")

    def clear(self):
        self.display.clear()

    def saveToFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Calculator History", "",
                                                  "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.display.text())

    def loadFromFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load Calculator History", "",
                                                  "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.display.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())
