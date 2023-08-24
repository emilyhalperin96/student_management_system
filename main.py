from PyQt6.QtWidgets import QApplication, QToolBar, QStatusBar, QComboBox, QTableWidgetItem, QTableWidget, QDialog, QMainWindow, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

import sqlite3
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setMinimumSize(800, 600)

        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&Help')
        edit_menu_item = self.menuBar().addMenu('&Edit')

        #Add a new student 

        add_student_action = QAction(QIcon('icons/add.png'), 'Add Student', self)
        add_student_action.triggered.connect(self.insert)


        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        #Show help at the top 
        about_action.setMenuRole(QAction.MenuRole.NoRole)


        search_action = QAction(QIcon('icons/search.png'), 'Search', self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)

        #Create table 
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False) #hide the first column
        self.setCentralWidget(self.table)

        # Create tool bar 
        toolbar = QToolBar()
        #user can move it around
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        #add elements to tool bar 
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Create status bar and add status bar elements 
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        #detect a self click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton('Edit Record')
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton('Delete Record')
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton) # clear buttons so there are no duplicates
        if children:
            for child in children:
                self.status_bar.removeWidget(child)


        self.status_bar.addWidget(edit_button)
        self.status_bar.addWidget(delete_button)
    
    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def search(self):
        dialog = InsertSearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()
    
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

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()

class DeleteDialog(QDialog):
    pass


class InsertSearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        button = QPushButton('Search')
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)
    
    def search(self):
        name = self.student_name.text()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM students WHERE name =?', (name,))
        rows = list(result)
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            main_window.table.item(item.row(), 
                                   1).setSelected(True)
        cursor.close()
        connection.close()
            


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        #Add Student Name Widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        # Add Combo box of courses
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        #Add Mobile Widget 
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('Mobile:')
        layout.addWidget(self.mobile)

        #Add Submit Button 
        button = QPushButton('Submit')
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)
    
    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_name.text()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO students (name, course, mobile) VALUES(?,?,?)', 
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        #loads the data 
        main_window.load_data()






app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())