# 🏋️ BMI Calculator — PyQt5 + MySQL

A sleek desktop application to calculate and track Body Mass Index (BMI) using Python, PyQt5, and MySQL.

<img width="1918" height="1142" alt="App Preview" src="https://github.com/user-attachments/assets/505309da-cc63-4867-b518-9af067b721b0" />

---

## 🚀 Features

- 🧮 Calculate BMI with instant feedback
- 💾 Save BMI records to a MySQL database
- 📊 View BMI history in a sortable table
- 🎨 Stylish and responsive PyQt5 interface

---

## 🛠️ Technologies Used

- Python 3
- PyQt5
- MySQL
- SQL

---

## 📦 setup Instructions
1. Clone the repository
   ```bash
   git clone https://github.com/codewithvikas96-ui/BMI-Calculator-PyQt5-MySQL.git
   ```
2. Navigate inside the project folder
   ```bash
   cd BMI-Calculator-PyQt5-MySQL
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. set up the MySQL Database
   - Open MySQL and create a database:
     ```sql
     CREATE DATABASE BodyMassIndex;
     ```
   - Use the database:
     ```sql
     USE BodyMassIndex;
     ```
     or just right click on the database (BodyMassIndex) and click on **Set as default Schema**
   - Create the users table:
     ```sql
     CREATE TABLE users (
          id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(100),
          weight DECIMAL(5,2),
          height DECIMAL(5,2),
          bmi DECIMAL(5,2),
          category VARCHAR(50),
          date_time DATETIME DEFAULT CURRENT_TIMESTAMP
      );
     ```

5. Run the application
   ```bash
   python src/main.py
   ```
---

## 🖼️ Schema Preview

<img width="1056" height="546" alt="MySQL Schema" src="https://github.com/user-attachments/assets/ee3dc62e-a5e1-4e9e-b923-b63c1ae0f217" />


<img width="909" height="419" alt="Table Preview" src="https://github.com/user-attachments/assets/1ccb78cc-0dd5-4f24-8219-cb67b28420e6" />

---

## 🧠 BMI Categories
| BMI Range | Category |
|:---------:|:--------:|
| < 18.5 | Underweight |
| 18.5 – 24.9	| Normal weight |
| 25 – 29.9 | Overweight |
| ≥ 30 | Obese |

---
## 💡 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📃 License
This project is licensed under the MIT License.

---

## 💡 Author
Made with 💛 by Vikas Ajay Vishwakarma
