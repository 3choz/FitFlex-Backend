CREATE TABLE [dbo].[tblExercise]
(
	[exID] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [exName] VARCHAR(75) NOT NULL, 
    [exDescription] VARCHAR(255) NOT NULL, 
    [exVideoLink] VARCHAR(255) NOT NULL, 
    [exTrainerSex] VARCHAR(6) NOT NULL, 
    [exVideoLength] TIME NOT NULL
)
