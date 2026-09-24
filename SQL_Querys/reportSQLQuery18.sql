USE ShetiMitra;
GO

SELECT
    C.CropName,
    SUM(S.Quantity * S.RatePerUnit) AS TotalSales
FROM Sales S
INNER JOIN Crops C
    ON S.CropID = C.CropID
GROUP BY C.CropName;


SELECT
    C.CropName,
    SUM(E.Amount) AS TotalExpenses
FROM Expenses E
INNER JOIN Crops C
    ON E.CropID = C.CropID
GROUP BY C.CropName;



SELECT
    C.CropName,
    ISNULL(
        (SELECT SUM(S.Quantity * S.RatePerUnit)
         FROM Sales S
         WHERE S.CropID = C.CropID), 0
    ) AS TotalSales,

    ISNULL(
        (SELECT SUM(E.Amount)
         FROM Expenses E
         WHERE E.CropID = C.CropID), 0
    ) AS TotalExpenses,

    ISNULL(
        (SELECT SUM(S.Quantity * S.RatePerUnit)
         FROM Sales S
         WHERE S.CropID = C.CropID), 0
    )
    -
    ISNULL(
        (SELECT SUM(E.Amount)
         FROM Expenses E
         WHERE E.CropID = C.CropID), 0
    ) AS Profit

FROM Crops C;



SELECT
    C.CropName,
    SUM(H.Quantity) AS TotalHarvest,
    H.Unit,
    H.Quality
FROM Harvest H
INNER JOIN Crops C
    ON H.CropID = C.CropID
GROUP BY
    C.CropName,
    H.Unit,
    H.Quality;


SELECT
    C.CropName,
    SUM(L.DaysWorked * L.WagePerDay) AS TotalLabourExpense
FROM Labour L
INNER JOIN Crops C
    ON L.CropID = C.CropID
GROUP BY C.CropName;



SELECT
    C.CropName,
    ISNULL(
        (SELECT SUM(F.Cost)
         FROM Fertilizers F
         WHERE F.CropID = C.CropID), 0
    ) AS FertilizerExpense,

    ISNULL(
        (SELECT SUM(P.Cost)
         FROM Pesticides P
         WHERE P.CropID = C.CropID), 0
    ) AS PesticideExpense

FROM Crops C;