# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectd.ui'
#
# Created by: PyQt6 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 451)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Username', 'Password', 'Nama'])
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")

        # we have connected clicked signal of button with the selec_data method
        self.pushButton.clicked.connect(self.select_data)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # this is the method for selecting data

    def select_data(self):
        try:
            mydb = mc.connect(

                host="localhost",
                user="root",
                password="",
                database="codeloop"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT username, password, nama FROM user")

            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                print(row_number)
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    # print(column_number)
                    self.tableWidget.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Show Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
