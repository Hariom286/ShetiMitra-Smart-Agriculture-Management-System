USE ShetiMitra;
GO

SELECT
    SUM(Quantity * RatePerUnit) AS TotalSales
FROM Sales;


SELECT
    SUM(Amount) AS TotalExpenses
FROM Expenses;



SELECT
    (SELECT SUM(Quantity * RatePerUnit) FROM Sales) AS TotalSales,
    (SELECT SUM(Amount) FROM Expenses) AS TotalExpenses,
    (SELECT SUM(Quantity * RatePerUnit) FROM Sales)
    -
    (SELECT SUM(Amount) FROM Expenses) AS TotalProfit;

