USE ShetiMitra;
GO

INSERT INTO Users (Username, PasswordHash, Role)
VALUES
('hariom', 'demo_hash_123', 'Farmer'),
('admin', 'demo_hash_456', 'Admin');
GO

SELECT * FROM Users;



INSERT INTO Farmers
(
    UserID,
    FarmerName,
    Mobile,
    Village,
    District
)
VALUES
(
    1,
    'Hariom Mane',
    '9876543210',
    'Wadgaon',
    'Latur'
);
GO

SELECT * FROM Farmers;