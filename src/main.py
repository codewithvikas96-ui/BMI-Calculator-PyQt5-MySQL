import mysql.connector
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,QMessageBox,
                             QTableWidget,QTableWidgetItem,QHeaderView)
from PyQt5.QtCore import Qt

db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "BodyMassIndex"
        )

cursor = db.cursor()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI CALCULATOR")
        self.BMI_UI()

    def BMI_UI(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        self.heading = QLabel("🏋🏻 BMI Calculator")
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("font-size: 40px; font-family: Oswald; color: navy;")
        main_layout.addWidget(self.heading)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.setFixedHeight(50)
        self.name_input.setStyleSheet("font-size: 40px; font-family: Times New Roman; color: hsl(120, 100%, 50%); background-color: black;")
        main_layout.addWidget(self.name_input)

        self.weight_input = QLineEdit(self)
        self.weight_input.setPlaceholderText("Enter your weight(in kilograms)")
        self.weight_input.setFixedHeight(50)
        self.weight_input.setStyleSheet("font-size: 40px; font-family: Times New Roman; color: hsl(120, 100%, 50%); background-color: black;")
        main_layout.addWidget(self.weight_input)

        self.height_input = QLineEdit(self)
        self.height_input.setPlaceholderText("Enter your height(in meters)")
        self.height_input.setFixedHeight(50)
        self.height_input.setStyleSheet("font-size: 40px; font-family: Times New Roman; color: hsl(120, 100%, 50%); background-color: black;")
        main_layout.addWidget(self.height_input)

        btn_layout = QHBoxLayout()
        
        self.bmi_btn = QPushButton("Calculate BMI")
        self.bmi_btn.setStyleSheet("font-size: 30px; color: white; background-color: hsl(344, 100%, 50%); font-family: Oswald; padding: 10px 20px; margin: 20px 10px; border: transparent; border-radius: 20px;")

        self.save_btn = QPushButton("Save BMI")
        self.save_btn.setStyleSheet("font-size: 30px; color: white; background-color: hsl(344, 100%, 50%); font-family: Oswald; padding: 10px 20px; margin: 20px 10px; border: transparent; border-radius: 20px;")

        self.record_btn = QPushButton("View History")
        self.record_btn.setStyleSheet("font-size: 30px; color: white; background-color: hsl(344, 100%, 50%); font-family: Oswald; padding: 10px 20px; margin: 20px 10px; border: transparent; border-radius: 20px;")

        self.bmi_btn.clicked.connect(self.calculate_bmi)
        self.save_btn.clicked.connect(self.save_data)
        self.record_btn.clicked.connect(self.view_records)

        btn_layout.addWidget(self.bmi_btn)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.record_btn)
        main_layout.addLayout(btn_layout)

        self.result_label = QLabel(self)
        self.result_label.setStyleSheet("font-size: 30px; font-family: Times New Roman; color: tomato;")
        main_layout.addWidget(self.result_label)

        self.table_widget = QTableWidget(self)
        main_layout.addWidget(self.table_widget)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            if not(30<= weight <= 300 and 1.0 <= height <= 2.5):
                raise ValueError
            
            bmi = weight / (height ** 2)
            category = self.bmi_category(bmi)
            self.result_label.setText(f"BMI: {bmi:.2f}\nCategory: {category}")
        except ValueError:
            self.result_label.clear()
            QMessageBox.warning(self,"Invalid Input!","Please enter valid height and weight")

    def bmi_category(self,bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"


    def save_data(self):
        name = self.name_input.text()
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            bmi = weight / (height ** 2)
            category = self.bmi_category(bmi)
            query = "INSERT INTO users (name,weight,height,bmi,category) VALUES (%s, %s, %s, %s, %s)"
            values = (name,weight,height,bmi,category)
            cursor.execute(query,values)
            db.commit()
            QMessageBox.information(self, "Saved", "Data Saved Successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        self.name_input.clear()
        self.weight_input.clear()
        self.height_input.clear()




    def view_records(self):
        cursor.execute("SELECT * FROM users ORDER BY date_time DESC")
        records = cursor.fetchall()

        if not records:
            QMessageBox.information(self, "No records", "No records found in the database")
            return
        
        self.table_widget.setRowCount(len(records))
        self.table_widget.setColumnCount(7)
        self.table_widget.setHorizontalHeaderLabels(["ID","Name","Weight","Height","BMI","Category","Date_Time"])
        self.table_widget.setAlternatingRowColors(True)

        self.table_widget.setStyleSheet("""
            QTableWidget {
                font-size: 14px;
                alternate-background-color: #f0f8ff;
                background-color: #ffffff;
            }
            QHeaderView::section {
                background-color: #add8e6;
                font-weight: bold;
                font-size: 15px;
                font-family: Arial;
            }
        """)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSortingEnabled(True)


        for row_idx, row_data in enumerate(records):
            for col_idx, item in enumerate(row_data):
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
             
        
        

def main():
    app = QApplication(sys.argv)
    my_window = Window()
    my_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    cursor.close()
    db.close()
