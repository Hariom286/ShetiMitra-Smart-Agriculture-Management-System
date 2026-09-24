USE ShetiMitra;
GO

CREATE TABLE Fertilizers
(
    FertilizerID INT IDENTITY(1,1) PRIMARY KEY,
    CropID INT NOT NULL,
    FertilizerName VARCHAR(100) NOT NULL,
    Quantity DECIMAL(10,2),
    FertilizerDate DATE,
    Cost DECIMAL(12,2),

    CONSTRAINT FK_Fertilizers_Crops
        FOREIGN KEY (CropID)
        REFERENCES Crops(CropID)
);
GO



CREATE TABLE Pesticides
(
    PesticideID INT IDENTITY(1,1) PRIMARY KEY,
    CropID INT NOT NULL,
    MedicineName VARCHAR(100) NOT NULL,
    PestDisease VARCHAR(150),
    Quantity DECIMAL(10,2),
    Unit VARCHAR(20),
    SprayDate DATE,
    Cost DECIMAL(12,2),

    CONSTRAINT FK_Pesticides_Crops
        FOREIGN KEY (CropID)
        REFERENCES Crops(CropID)
);
GO


CREATE TABLE Labour
(
    LabourID INT IDENTITY(1,1) PRIMARY KEY,
    CropID INT NOT NULL,
    WorkerName VARCHAR(100) NOT NULL,
    WorkType VARCHAR(100),
    WorkDate DATE,
    DaysWorked DECIMAL(5,2),
    WagePerDay DECIMAL(10,2),
    TotalWage AS (DaysWorked * WagePerDay),

    CONSTRAINT FK_Labour_Crops
        FOREIGN KEY (CropID)
        REFERENCES Crops(CropID)
);
GO

