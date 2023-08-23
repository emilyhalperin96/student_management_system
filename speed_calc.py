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

        self.metric_label = QComboBox()
        self.metric_label.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton('Calculate Speed')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        #Add Widgets to grid

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(self.metric_label, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2) #span accross one row and 2 columns 
        grid.addWidget(self.output_label, 3, 0, 1, 2) #span accross one row and 2 columns 

        
        self.setLayout(grid)

    
    def calculate_speed(self):
        #get distance and time from input 
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())

        #speed 
        speed = distance/time 

        #check combo 

        if self.metric_label.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            unit = 'km/h'
        if self.metric_label.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621361, 2)
            unit = 'mph'
        
        #display result
        

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())