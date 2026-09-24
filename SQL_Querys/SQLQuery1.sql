CREATE DATABASE ShetiMitra;
GO

USE ShetiMitra;
GO

CREATE TABLE Users
(
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    Role VARCHAR(20) NOT NULL
);
GO

CREATE TABLE Farmers
(
    FarmerID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    FarmerName VARCHAR(100) NOT NULL,
    Mobile VARCHAR(15),
    Village VARCHAR(100),
    District VARCHAR(100),

    CONSTRAINT FK_Farmers_Users
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
);
GO
CREATE TABLE Farms
(
    FarmID INT IDENTITY(1,1) PRIMARY KEY,
    FarmerID INT NOT NULL,
    FarmName VARCHAR(100),
    Area DECIMAL(10,2),
    SoilType VARCHAR(50),
    IrrigationType VARCHAR(50),
    WaterSource VARCHAR(100),
    Location VARCHAR(200),

    CONSTRAINT FK_Farms_Farmers
        FOREIGN KEY (FarmerID)
        REFERENCES Farmers(FarmerID)
);
GO

SELECT * FROM Users;
SELECT * FROM Farmers;
SELECT * FROM Farms;