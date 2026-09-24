USE ShetiMitra;
GO

CREATE TABLE Weather
(
    WeatherID INT IDENTITY(1,1) PRIMARY KEY,
    FarmID INT NOT NULL,
    WeatherDate DATE NOT NULL,
    Temperature DECIMAL(5,2),
    Rainfall DECIMAL(8,2),
    Humidity DECIMAL(5,2),
    WindSpeed DECIMAL(6,2),
    WeatherCondition VARCHAR(100),

    CONSTRAINT FK_Weather_Farms
        FOREIGN KEY (FarmID)
        REFERENCES Farms(FarmID)
);
GO