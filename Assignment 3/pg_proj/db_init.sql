PRAGMA foreign_keys = ON;

DROP TABLE Tasks;

/*
CREATE TABLE Tasks (
    taskID INTEGER PRIMARY KEY,
    userID INTEGER,
    -- FOREIGN KEY (userID) REFERENCES Users(userID),
    isComplete INTEGER,
    taskLabel VARCHAR(255),
    priority INTEGER,
    forceDependency INTEGER
);
*/