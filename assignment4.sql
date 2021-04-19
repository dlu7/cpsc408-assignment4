-- movie info
CREATE TABLE IF NOT EXISTS Movie(
    MovieID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(50),
    Year SMALLINT,
    Genre VARCHAR(50),
    ContentRating VARCHAR(6),
    Director VARCHAR(50),
    RunningTime VARCHAR(50),
    Actor1 VARCHAR(50),
    Actor2 VARCHAR(50),
    Actor3 VARCHAR(50),
    Actor4 VARCHAR(50),
    AvgRating TINYINT
);

-- user info
CREATE TABLE IF NOT EXISTS User(
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(50)
);

-- plan to watch
CREATE TABLE IF NOT EXISTS Planned(
    UserID INT,
    MovieID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID)
);

-- already watched
CREATE TABLE IF NOT EXISTS Watched(
    UserID INT,
    MovieID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID)
);

-- ratings
CREATE TABLE IF NOT EXISTS UserRating(
    UserID INT,
    MovieID INT,
    Rating TINYINT,
    Review VARCHAR(250),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID)
);