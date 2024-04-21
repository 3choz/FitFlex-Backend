CREATE TABLE [dbo].[tblProgram]
(
	[prgmID] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [prgmName] VARCHAR(255) NOT NULL, 
    [prgmDescription] VARCHAR(255) NOT NULL 
)
