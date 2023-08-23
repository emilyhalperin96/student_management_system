from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime

class AgeCalculator(QWidget):

    def __init__(self):

        #returns the parent of the class that you're calling
        super().__init__()
        grid = QGridLayout()


        # Create Widgets
        name_label = QLabel('Name: ')
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel('Date of Birth MM/DD/YYYY: ')
        #make it an instance variable so that we can access it in the calculate_age function
        self.date_bith_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate Age')
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel('')

        # Add Widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_bith_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2) #span accross one row and 2 columns 
        grid.addWidget(self.output_label, 3, 0, 1, 2) #span accross one row and 2 columns 

        self.setLayout(grid)
    
    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_bith_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y').date().year
        age = current_year - year_of_birth
        self.output_label.setText(f'{self.name_line_edit.text()} is {age} years old')
        


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())