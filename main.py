import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from versand import *


# Fenster
app = QApplication(sys.argv)
window = QMainWindow()
ui =Ui_mainWindow()
ui.setupUi(window)
window.show()


sys.exit(app.exec_())