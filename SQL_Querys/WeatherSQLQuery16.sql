USE ShetiMitra;
GO

INSERT INTO Weather
(
    FarmID,
    WeatherDate,
    Temperature,
    Rainfall,
    Humidity,
    WindSpeed,
    WeatherCondition
)
VALUES
(
    1,
    '2026-09-12',
    28.50,
    2.40,
    72.00,
    12.50,
    'Partly Cloudy'
);
GO

SELECT * FROM Weather;