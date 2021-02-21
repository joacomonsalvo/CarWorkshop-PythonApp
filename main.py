"Native Modules"
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def windows(xpos, ypos, width, hight):
    "Window"
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

windows(200, 200, 300, 300)
