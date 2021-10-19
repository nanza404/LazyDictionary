from PyQt6.QtWidgets import QApplication
import sys
import Dictgui

app = QApplication(sys.argv)
window = Dictgui.Window()
window.show()
sys.exit(app.exec())
