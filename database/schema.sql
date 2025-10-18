CREATE DATABASE BodyMassIndex;
USE BodyMassIndex;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    weight DECIMAL(5,2),
    height DECIMAL(5,2),
    bmi DECIMAL(5,2),
    category VARCHAR(50),
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
