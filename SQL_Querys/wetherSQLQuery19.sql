USE ShetiMitra;
GO

SELECT
    F.FarmName,
    W.WeatherDate,
    W.Temperature,
    W.Rainfall,
    W.Humidity,
    W.WindSpeed,
    W.WeatherCondition
FROM Weather W
INNER JOIN Farms F
    ON W.FarmID = F.FarmID
ORDER BY W.WeatherDate DESC;