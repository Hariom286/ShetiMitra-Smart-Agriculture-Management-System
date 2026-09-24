USE ShetiMitra;
GO

INSERT INTO Farms
(
    FarmerID,
    FarmName,
    Area,
    SoilType,
    IrrigationType,
    WaterSource,
    Location
)
VALUES
(
    1,
    'Main Farm',
    2.50,
    'Black Soil',
    'Drip',
    'Pipeline',
    'Latur'
);
GO

SELECT * FROM Farms;