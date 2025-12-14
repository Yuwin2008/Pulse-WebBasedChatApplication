CREATE DATABASE Pulse;
USE Pulse;

-- ================= USERS TABLE =================
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- ================= POSTS TABLE =================
CREATE TABLE Posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    content VARCHAR(1000),
    likes INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
