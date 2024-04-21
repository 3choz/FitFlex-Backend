CREATE TABLE [dbo].[tblPassword]
(
	[passID] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [passSalt] VARCHAR(255) NOT NULL, 
    [passHash] VARCHAR(255) NOT NULL
)
