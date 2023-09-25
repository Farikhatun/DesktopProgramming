# login_gui.py
# Import necessary modules
import sys
import mysql.connector
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from registrasi import RegisterForm


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def setUpWindow(self):
        """Create and arrange widgets in the main window."""
        self.login_is_successful = False

        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(160, 10)

        # Create widgets for username and password
        username_label = QLabel("Username:", self)
        username_label.move(20, 54)
        self.username_edit = QLineEdit(self)
        self.username_edit.resize(250, 24)
        self.username_edit.move(90, 50)
        password_label = QLabel("Password:", self)
        password_label.move(20, 86)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(
            QLineEdit.EchoMode.Password)
        self.password_edit.resize(250, 24)
        self.password_edit.move(90, 82)

        # Create QCheckBox for displaying password
        self.show_password_cb = QCheckBox(
            "Show Password", self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(
            self.displayPasswordIfChecked)

        # Create QPushButton for signing in
        login_button = QPushButton("Login", self)
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        # Create sign up QLabel and QPushButton
        not_member_label = QLabel("Not a Member?", self)
        not_member_label.move(20, 186)
        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.move(170, 180)
        sign_up_button.clicked.connect(self.createNewUser)

    def clickLoginButton(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="codeloop"
        )

        mycursor = mydb.cursor()

        # Check if username and password are correct
        sql = "SELECT * FROM user WHERE username = %s AND password = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            QMessageBox.information(
                self, 'Information Message', 'Login Successful!', QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.warning(self, "Error Message", "The username or password is incorrect.",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

# login_gui.py
    def displayPasswordIfChecked(self, checked):
        """If QCheckButton is enabled, view the password.
        Else, mask the password so others can not see it."""
        if checked:
            self.password_edit.setEchoMode(
                QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.password_edit.setEchoMode(
                QLineEdit.EchoMode.Password)

    def createNewUser(self):
        """Open a dialog for creating a new account."""
        self.create_new_user_window = RegisterForm()
        self.create_new_user_window.show()

    def openApplicationWindow(self):
        """Open a mock main window after the user logs in."""
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self, event):
        """Reimplement the closing event to display a
        QMessageBox before closing."""
        if self.login_is_successful == True:
            event.accept()
        else:
            answer = QMessageBox.question(
                self, "Quit Application?",
                "Are you sure you want to QUIT?",
                QMessageBox.StandardButton.No |
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            if answer == QMessageBox.StandardButton.No:
                event.ignore()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(360, 220)
        self.setWindowTitle("Login")
        self.setUpWindow()
        self.show()

    def setUpMainWindow(self):
        image = "images/swan.jpg"
        try:
            with open(image):
                user_label = QLabel(self)
                pixmap = QPixmap(image)
                user_label.setPixmap(pixmap)
                user_label.move(150, 60)
        except FileNotFoundError as error:
            print(f"Image not found. Error: {error}")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(640, 426)
        self.setWindowTitle('3.1 – Main Window')
        self.setUpMainWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
