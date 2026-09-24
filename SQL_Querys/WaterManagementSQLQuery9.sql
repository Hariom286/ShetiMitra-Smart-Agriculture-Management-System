USE ShetiMitra;
GO

INSERT INTO WaterManagement
(
    CropID,
    WaterDate,
    WateringTime,
    IrrigationMethod
)
VALUES
(
    1,
    '2026-09-12',
    30,
    'Drip'
);
GO

SELECT * FROM WaterManagement;