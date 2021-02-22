"Native Modules"
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    "Big class"

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Vehicles App")
        self.init_ui()

    def init_ui(self):
        "Create Label and button1"
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My first Label')
        self.label.move(100, 100)

        #Create button
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click me")
        self.button.clicked.connect(self.click)

    def click(self):
        "Click"
        self.label.setText("You pressed the button")
        self.update()


    def update(self):
        "Update Size"
        self.label.adjustSize()


def windows():
    "Window"
    app = QApplication(sys.argv) # Config set up for qt app
    win = MyWindow()
    win.show() #Show the window
    sys.exit(app.exec_()) # Make cross bottom work

windows()
