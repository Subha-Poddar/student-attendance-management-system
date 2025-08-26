CREATE DATABASE student_attendance;
USE student_attendance;
CREATE TABLE students (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    roll_number VARCHAR(20) UNIQUE,
    class VARCHAR(20)
);

CREATE TABLE attendance (
    attendance_id INT IDENTITY(1,1) PRIMARY KEY,
    student_id INT,
    date DATE,
    status VARCHAR(10),  
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);


CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100),
    role VARCHAR(20) CHECK (role IN ('admin', 'teacher'))
);

-- Sample users
INSERT INTO users (username, password, role) VALUES ('admin', 'adminpass', 'admin');
INSERT INTO users (username, password, role) VALUES ('teacher', 'teacherpass', 'teacher');

select * from students;
select * from attendance;
select * from users;

