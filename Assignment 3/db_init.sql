CREATE DATABASE Tasks;
USE Tasks;

CREATE TABLE UserTypes (
    userTypeID INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(255) NOT NULL
);

CREATE TABLE Users (
    userID INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    hashedPassword CHAR(64) NOT NULL,
    userTypeID INT,
    FOREIGN KEY (userTypeID) REFERENCES UserTypes(userTypeID)
);

CREATE TABLE Tasks (
    taskID INT PRIMARY KEY AUTO_INCREMENT,
    userID INT,
    FOREIGN KEY (userID) REFERENCES Users(userID),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    due TIMESTAMP,
    reminder TIMESTAMP,
    isComplete BOOLEAN,
    taskLabel VARCHAR(255),
    priority INT,
    forceDependency BOOLEAN
);

CREATE TABLE Dependencies (
    dependencyID INT PRIMARY KEY AUTO_INCREMENT,
    parentTask INT,
    dependentTask INT,
    FOREIGN KEY (parentTask) REFERENCES Tasks(taskID),
    FOREIGN KEY (dependentTask) REFERENCES Tasks(taskID)
);

CREATE TABLE Media (
    mediaID INT PRIMARY KEY AUTO_INCREMENT,
    userID INT,
    FOREIGN KEY (userID) REFERENCES Users(userID),
    taskID INT,
    FOREIGN KEY (taskID) REFERENCES Tasks(taskID),
    uploaded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    label VARCHAR(255),
    fsPath VARCHAR(255)
);

CREATE TABLE TaskNotes (
    noteID INT PRIMARY KEY AUTO_INCREMENT,
    taskID INT,
    FOREIGN KEY (taskID) REFERENCES Tasks(taskID),
    userID INT,
    FOREIGN KEY (userID) REFERENCES Users(userID),
    noteData VARCHAR(255)
);