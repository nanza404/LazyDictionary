from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys
import main


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LazyDictionary')
        self.setWindowIcon(QIcon('book.png'))
        self.setFixedHeight(70)
        self.setFixedWidth(300)
        self.button()
        self.oneClick = True

    def button(self):
        self.btn0 = QPushButton('Start', self)
        self.btn0.setGeometry(0, 0, 150, 70)
        self.btn0.setStyleSheet('background-color:green')
        self.btn0.setFont(QFont('san serif', 15))
        self.btn1 = QPushButton('Stop', self)
        self.btn1.setGeometry(150, 0, 150, 70)
        self.btn1.setStyleSheet('background-color:grey')
        self.btn1.setFont(QFont('san serif', 15))

        self.btn0.clicked.connect(self.clickButton0)
        self.btn1.clicked.connect(self.clickButton1)

    def clickButton0(self):
        self.btn0.setStyleSheet('background-color:grey')
        self.btn1.setStyleSheet('background-color:red')
        if self.oneClick:
            main.start()
        self.oneClick = False

    def clickButton1(self):
        self.btn1.setStyleSheet('background-color:grey')
        self.btn0.setStyleSheet('background-color:green')
        main.end()
        self.oneClick = True


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
