import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form Registrasi')
        self.setFixedSize(360, 320)

        # Labels
        self.username_label = QLabel('Username:')
        self.password_label = QLabel('Password:')
        self.nama_label = QLabel('Nama:')

        # Line Edits
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.nama_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        # Button
        self.submit_button = QPushButton('Registrasi')
        self.submit_button.clicked.connect(self.submit)

        # Error Label
        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: red")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.nama_label)
        layout.addWidget(self.nama_edit)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.error_label)
        self.setLayout(layout)

    def submit(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        nama = self.nama_edit.text()

        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="codeloop"
        )

        mycursor = mydb.cursor()

        # Insert data into MySQL database
        sql = "INSERT INTO user (username, password, nama) VALUES (%s, %s, %s)"
        val = (username, password, nama)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(f'{mycursor.rowcount} data berhasil disimpan.')
        except mysql.connector.Error as error:
            self.error_label.setText(str(error))
            mydb.rollback()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegisterForm()
    form.show()
    sys.exit(app.exec())
