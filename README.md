# Student-Performance-Prediction
🎓 Student Performance Prediction System (Role-Based Web Application)
📌 Project Description

The Student Performance Prediction System is a role-based web application that predicts a student’s academic outcome (Pass / Fail) using Machine Learning techniques.
The system allows teachers to manage student academic data and students to securely log in and view their performance prediction in real time.

This project integrates Machine Learning, Database Management, and Web Development to create a realistic academic analytics system.

🎯 Objectives

Predict student academic performance using Machine Learning

Provide secure login for students and teachers

Allow teachers to update attendance, marks, study hours, and CGPA

Enable students to view their data and performance prediction

Demonstrate practical application of ML concepts in a real-world scenario

👥 User Roles
👨‍🏫 Teacher

Secure login

Add or update student academic details:

Attendance

Internal Marks

Study Hours

Previous Semester CGPA

🎓 Student

Secure login using Student ID

View personal academic data

Predict performance (Pass / Fail) using ML model

🤖 Machine Learning Concepts Used

Logistic Regression

Feature Scaling (StandardScaler)

Classification Probability Thresholding

Performance Prediction

🛠️ Technologies Used
Category	Tools
Programming Language	Python
Web Framework	Flask
Database	SQLite
ML Libraries	Scikit-learn
Data Handling	Pandas, NumPy
Frontend	HTML, CSS
🗂️ Project Features

Role-based authentication system

Real-time ML prediction via web interface

Database-driven student records

Clean and modular Flask architecture

Scalable and extendable design

🧠 How It Works

Teacher logs in and updates student academic details

Data is stored securely in SQLite database

Student logs in using their ID

Machine Learning model processes student data

System predicts Pass / Fail with probability score

student_performance_web/

│
├── app.py

├── model.py

├── database.db

│

├── templates/


│       ├── login.html

│       ├── student_dashboard.html

│       ├── teacher_dashboard.html

│

└── static/

    └── style.css
    

🚀 Future Enhancements

Grade prediction (A/B/C)

Graphical analytics dashboard

Admin role management

Password hashing & security improvements

Cloud deployment (Render / PythonAnywhere)

📌 Conclusion

This project demonstrates the practical integration of Machine Learning, Flask web development, and database systems to solve a real-world academic problem.
It is suitable for academic mini-projects, final-year projects, and resume portfolios.
