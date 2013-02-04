import sys
from PyQt4 import QtCore, QtGui
from ui_mainwindow import Ui_MainWindow

class DemoWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self) 
        self.setupUi(self)
