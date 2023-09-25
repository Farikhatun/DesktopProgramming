from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import mysql.connector
import sys
import MySQLdb as mdb


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Database Connection"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.button = QPushButton('DB Connection', self)
        self.button.setGeometry(100, 100, 200, 50)
        self.button.clicked.connect(self.DBConnection)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def DBConnection(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ptikuns"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT nama, nim, email FROM mahasiswa")
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)

        except mdb.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            sys.exit(1)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
