USE ShetiMitra;
GO

CREATE TABLE Expenses
(
    ExpenseID INT IDENTITY(1,1) PRIMARY KEY,
    CropID INT NOT NULL,
    ExpenseDate DATE NOT NULL,
    ExpenseType VARCHAR(50) NOT NULL,
    Description VARCHAR(200),
    Amount DECIMAL(12,2) NOT NULL,

    CONSTRAINT FK_Expenses_Crops
        FOREIGN KEY (CropID)
        REFERENCES Crops(CropID)
);
GO



CREATE TABLE Harvest
(
    HarvestID INT IDENTITY(1,1) PRIMARY KEY,
    CropID INT NOT NULL,
    HarvestDate DATE NOT NULL,
    Quantity DECIMAL(12,2) NOT NULL,
    Unit VARCHAR(20) NOT NULL,
    Quality VARCHAR(50),

    CONSTRAINT FK_Harvest_Crops
        FOREIGN KEY (CropID)
        REFERENCES Crops(CropID)
);
GO



CREATE TABLE Sales
(
    SaleID INT IDENTITY(1,1) PRIMARY KEY,
    CropID INT NOT NULL,
    SaleDate DATE NOT NULL,
    BuyerName VARCHAR(100),
    Quantity DECIMAL(12,2) NOT NULL,
    Unit VARCHAR(20) NOT NULL,
    RatePerUnit DECIMAL(12,2) NOT NULL,
    TotalAmount AS (Quantity * RatePerUnit),

    CONSTRAINT FK_Sales_Crops
        FOREIGN KEY (CropID)
        REFERENCES Crops(CropID)
);
GO