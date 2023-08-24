from PyQt6.QtWidgets import QApplication, QComboBox, QTableWidgetItem, QTableWidget, QDialog, QMainWindow, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QAction

import sqlite3
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')

        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&Help')

        #Add a new student 

        add_student_action = QAction('Add Student', self)
        add_student_action.triggered.connect(self.insert)


        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        #Show help at the top 
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        #Create table 
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False) #hide the first column
        self.setCentralWidget(self.table)
    
    def load_data(self):
        #create connection
        connection = sqlite3.connect('database.db')
        result = connection.execute('SELECT * FROM students')
        self.table.setRowCount(0) #avoid duplicate data

        #populate code with data
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()
    
    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        #Add Student Name Widget
        student_name = QLineEdit()
        student_name.setPlaceholderText('Name')
        layout.addWidget(student_name)

        # Add Combo box of courses
        course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        course_name.addItems(courses)
        layout.addWidget(course_name)

        self.setLayout(layout)





app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
age_calculator.load_data()
sys.exit(app.exec())