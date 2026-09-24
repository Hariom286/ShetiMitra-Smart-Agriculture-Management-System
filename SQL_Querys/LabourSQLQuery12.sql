USE ShetiMitra;
GO

INSERT INTO Labour
(
    CropID,
    WorkerName,
    WorkType,
    WorkDate,
    DaysWorked,
    WagePerDay
)
VALUES
(
    1,
    'Ramesh',
    'Weeding',
    '2026-09-12',
    2.00,
    500.00
);
GO

SELECT * FROM Labour;