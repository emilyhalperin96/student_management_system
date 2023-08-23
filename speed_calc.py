from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
import sys
from datetime import datetime

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        #Create Widgets 
        distance_label = QLabel('Distance:')
        self.distance_label_edit = QLineEdit()

        time_label = QLabel('Time (hours):')
        self.time_label_edit = QLineEdit()

        metric_label = QComboBox()
        metric_label.addItems(['km', 'other'])

        if metric_label.currentText() == 'km':
            'do something'
        if metric_label.currentText() == 'other':
            'do something else'

        calculate_button = QPushButton('Calculate Speed')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        #Add Widgets to grid

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2) #span accross one row and 2 columns 
        grid.addWidget(self.output_label, 3, 0, 1, 2) #span accross one row and 2 columns 

        grid.addWidget(metric_label, 2, 2)
        
        self.setLayout(grid)

    
    def calculate_speed(self):
        speed = self.distance_label_edit.text() // self.time_label_edit.text()
        self.output_label.setText('f Average Speed: speed')


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())