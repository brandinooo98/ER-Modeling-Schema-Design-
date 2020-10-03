DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Bids;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Rating;
DROP TABLE IF EXISTS LineItem;
DROP TABLE IF EXISTS Category;

CREATE TABLE Item (
    itemID			INT NOT NULL UNIQUE,
    name			INT NOT NULL,
    buy_price		DOUBLE,
    first_bid		DOUBLE NOT NULL,
    number_of_bids	INT NOT NULL,
    currently		DOUBLE NOT NULL,
    started			CHAR (255) NOT NULL,
    ends			CHAR (255) NOT NULL,
    PRIMARY KEY (itemID),
    FOREIGN KEY (locationID) REFERENCE Location (locationID)
);

CREATE TABLE Bids (
    bidsID INT NOT NULL UNIQUE,
    userID INT NOT NULL UNIQUE,
    time CHAR (255) NOT NULL,
    amount CHAR (255) NOT NULL,
    PRIMARY KEY (bidsID)
);

CREATE TABLE User (
    userID INT NOT NULL UNIQUE,
    locationID INT,
    countryID INT,
    ratingID INT NOT NULL,
    bidsID INT NOT NULL,
    PRIMARY KEY (userID)
    FOREIGN KEY (locationID) REFERENCE Location (locationID),
    FOREIGN KEY (countryID) REFERENCE Country (countryID),
    FOREIGN KEY (ratingID) REFERENCE Rating (ratingID),
);

CREATE TABLE Location (
    locationID INT NOT NULL UNIQUE,
    countryID INT NOT NULL,
    location CHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (locationID),
    FOREIGN KEY (countryID) REFERENCE Country (countryID)
);

CREATE TABLE Country (
    countryID INT NOT NULL UNIQUE,
    country CHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (countryID)
);

CREATE TABLE Rating (
    ratingID INT NOT NULL UNIQUE,
    rating CHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (ratingID)
);

CREATE TABLE LineItem (
    categoryID INT NOT NULL UNIQUE,
    itemID INT NOT NULL UNIQUE,
    FOREIGN KEY (categoryID) REFERENCE Category (categoryID),
    FOREIGN KEY (itemID) REFERENCE Item (itemID)
);

CREATE TABLE Category (
    categoryID INT NOT NULL UNIQUE,
    category CHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (categoryID)
);
