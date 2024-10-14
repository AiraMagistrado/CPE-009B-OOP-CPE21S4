import sys
from PyQt5.QtWidgets import QApplication
from registration import RegistrationApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationApp()
    sys.exit(app.exec_())