USE ShetiMitra;
GO

INSERT INTO Fertilizers
(
    CropID,
    FertilizerName,
    Quantity,
    FertilizerDate,
    Cost
)
VALUES
(
    1,
    'Urea',
    25.00,
    '2026-09-10',
    700.00
);
GO

SELECT * FROM Fertilizers;