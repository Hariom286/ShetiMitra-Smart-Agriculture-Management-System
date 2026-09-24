USE ShetiMitra;
GO

INSERT INTO Harvest
(
    CropID,
    HarvestDate,
    Quantity,
    Unit,
    Quality
)
VALUES
(
    1,
    '2026-12-15',
    2500.00,
    'kg',
    'Good'
);
GO

SELECT * FROM Harvest;