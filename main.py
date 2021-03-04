from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        "Label"
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 140, 381, 241))
        
        font = QtGui.QFont()
        font.setPointSize(36)
        
        self.label.setFont(font)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        
        "MenuBar"
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName('menubar')

        "File"
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName('menuFile')

        MainWindow.setMenuBar(self.menubar)

        "StatusBar"
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        "Shortcuts"
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSave.setObjectName('actionSave')

        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'CarWorkshop'))
        self.label.setText(_translate("CarWorkshop", "TextLabel"))
        self.menuFile.setTitle(_translate('MainWindow', 'File'))
        
        self.actionSave.setText(_translate('MainWindow', 'Save'))
        self.actionSave.setStatusTip(_translate('MainWindow', 'Save a file'))
        self.actionSave.setShortcut(_translate('MainWindow', 'Ctrl+S'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) # Config set up for qt app
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) # Make cross bottom work
