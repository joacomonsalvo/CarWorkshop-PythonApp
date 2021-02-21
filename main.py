# consoleprogram.py but with the visual interface

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 200
ypos = 200
width = 300
hight = 300

def windows(xpos, ypos, width, hight):
    app = QApplication(sys.argv) # Config set up for qt app
    win = QMainWindow() # Create the window/widget that is shown
    win.setGeometry(xpos, ypos, width, hight) # Set dimensions
    win.setWindowTitle('Vehicles App') # Title that the windows shows at the top

    #Label
    label = QtWidgets.QLabel(win)
    label.setText('My first Label')
    label.move(100, 100)

    win.show() #Show the window
    sys.exit(app.exec_()) # Make cross bottom work

windows(xpos, ypos, width, hight)
