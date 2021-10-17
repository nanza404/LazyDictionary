from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys
#import os
#sys.path.append(os.path.dirname(os.path.abspath(main.py)))
import main



class Window(QWidget):
    global running
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LazyDictionary')
        self.setWindowIcon(QIcon('book.png'))
        self.setFixedHeight(100)
        self.setFixedWidth(300)
        self.button()

    def button(self):
        self.btn0 = QPushButton('Start', self)
        self.btn0.setGeometry(0, 30, 150, 70)
        self.btn0.setStyleSheet('background-color:green')
        self.btn0.setFont(QFont('san serif', 15))
        self.btn1 = QPushButton('Stop', self)
        self.btn1.setGeometry(150, 30, 150, 70)
        self.btn1.setStyleSheet('background-color:grey')
        self.btn1.setFont(QFont('san serif', 15))

        self.btn0.clicked.connect(self.clickButton0)
        self.btn1.clicked.connect(self.clickButton1)

    def clickButton0(self):
        self.btn0.setStyleSheet('background-color:grey')
        self.btn1.setStyleSheet('background-color:red')
        main.keyLog.keyLogger()
        

    def clickButton1(self):
        self.btn1.setStyleSheet('background-color:grey')
        self.btn0.setStyleSheet('background-color:green')
        print('stopped')
        running = False


app = QApplication(sys.argv)

window = Window()


window.show()
sys.exit(app.exec())
