DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Bid;
DROP TABLE IF EXISTS Bidder;
DROP TABLE IF EXISTS Seller;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS LineItem;
DROP TABLE IF EXISTS Category;

CREATE TABLE Item (
    itemID INT NOT NULL UNIQUE,
    locationID INT,
    name INT NOT NULL,
    first_bid DOUBLE NOT NULL,
    number_of_bids INT NOT NULL,
    currently DOUBLE NOT NULL,
    started CHAR (255) NOT NULL,
    ends CHAR (255) NOT NULL,
    PRIMARY KEY (itemID),
    FOREIGN KEY (locationID) REFERENCES Location (locationID)
);

CREATE TABLE Bid (
    bidsID INT NOT NULL UNIQUE,
    userID INT NOT NULL,
    time CHAR (255) NOT NULL,
    amount CHAR (255) NOT NULL,
    itemID INT NOT NULL,
    PRIMARY KEY (bidsID)
);

CREATE TABLE Bidder (
    userID INT NOT NULL UNIQUE,
    locationID INT,
    countryID INT,
    rating DOUBLE NOT NULL,
    PRIMARY KEY (userID),
    FOREIGN KEY (locationID) REFERENCES Location (locationID),
    FOREIGN KEY (countryID) REFERENCES Country (countryID)
);

CREATE TABLE Seller (
    userID INT NOT NULL UNIQUE,
    locationID INT,
    countryID INT,
    rating DOUBLE NOT NULL,
    PRIMARY KEY (userID),
    FOREIGN KEY (locationID) REFERENCES Location (locationID),
    FOREIGN KEY (countryID) REFERENCES Country (countryID)
);

CREATE TABLE Location (
    locationID INT NOT NULL UNIQUE,
    location CHAR(255) UNIQUE,
    PRIMARY KEY (locationID)
);

CREATE TABLE Country (
    countryID INT NOT NULL UNIQUE,
    country CHAR(255) UNIQUE,
    PRIMARY KEY (countryID)
);

CREATE TABLE LineItem (
    categoryID INT NOT NULL,
    itemID INT NOT NULL,
    FOREIGN KEY (categoryID) REFERENCES Category (categoryID),
    FOREIGN KEY (itemID) REFERENCES Item (itemID)
);

CREATE TABLE Category (
    categoryID INT NOT NULL UNIQUE,
    category CHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (categoryID)
);
