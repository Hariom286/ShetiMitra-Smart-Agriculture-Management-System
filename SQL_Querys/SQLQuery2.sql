USE ShetiMitra;
GO

CREATE TABLE Crops
(
    CropID INT IDENTITY(1,1) PRIMARY KEY,
    FarmID INT NOT NULL,
    CropName VARCHAR(100) NOT NULL,
    Season VARCHAR(50),
    Area DECIMAL(10,2),
    SowingDate DATE,
    ExpectedHarvestDate DATE,

    CONSTRAINT FK_Crops_Farms
        FOREIGN KEY (FarmID)
        REFERENCES Farms(FarmID)
);
GO
CREATE TABLE WaterManagement
(
    WaterID INT IDENTITY(1,1) PRIMARY KEY,
    CropID INT NOT NULL,
    WaterDate DATE NOT NULL,
    WateringTime INT,
    IrrigationMethod VARCHAR(50),

    CONSTRAINT FK_Water_Crops
        FOREIGN KEY (CropID)
        REFERENCES Crops(CropID)
);
GO