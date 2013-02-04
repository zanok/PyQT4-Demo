#!/usr/bin/python
import sys

from PyQt4 import QtCore, QtGui
from demowindow import DemoWindow

app = QtGui.QApplication(sys.argv)
form = DemoWindow()
form.show()
app.exec_()
