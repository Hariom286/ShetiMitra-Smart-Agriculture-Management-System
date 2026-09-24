USE ShetiMitra;
GO

INSERT INTO Pesticides
(
    CropID,
    MedicineName,
    PestDisease,
    Quantity,
    Unit,
    SprayDate,
    Cost
)
VALUES
(
    1,
    'Neem Oil',
    'Aphids',
    500.00,
    'ml',
    '2026-09-11',
    250.00
);
GO

SELECT * FROM Pesticides;