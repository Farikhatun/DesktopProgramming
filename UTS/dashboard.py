from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def _init_(self):
        super()._init_()
        self.resize(300, 300)
        self.setWindowTitle("Dashboard")
        self.setWindowIcon(QIcon("images/background.jpg"))

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Hello world")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
