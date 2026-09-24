USE ShetiMitra;
GO

INSERT INTO Expenses
(
    CropID,
    ExpenseDate,
    ExpenseType,
    Description,
    Amount
)
VALUES
(
    1,
    '2026-09-12',
    'Labour',
    'Weeding work',
    1000.00
);
GO

SELECT * FROM Expenses;