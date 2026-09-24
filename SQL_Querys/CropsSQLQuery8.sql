USE ShetiMitra;
GO

INSERT INTO Crops
(
    FarmID,
    CropName,
    Season,
    Area,
    SowingDate,
    ExpectedHarvestDate
)
VALUES
(
    1,
    'Beetroot',
    'Rabi',
    2.50,
    '2026-09-01',
    '2026-12-15'
);
GO

SELECT * FROM Crops;