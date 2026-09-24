USE ShetiMitra;
GO

INSERT INTO Sales
(
    CropID,
    SaleDate,
    BuyerName,
    Quantity,
    Unit,
    RatePerUnit
)
VALUES
(
    1,
    '2026-12-18',
    'Local Market',
    2500.00,
    'kg',
    20.00
);
GO

SELECT * FROM Sales;