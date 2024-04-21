CREATE TABLE [dbo].[tblUserExercise]
(
	[ueID] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [exID] INT NULL, 
    [userEmail] VARCHAR(75) NULL, 
    [ueDate] DATE NULL, 
    [ueType] VARCHAR(75) NULL, 
    [ueAmount] DECIMAL(18, 2) NULL, 
    CONSTRAINT [FK_tblUserExercise_tblExercise] FOREIGN KEY ([exID]) REFERENCES [tblExercise]([exID]),
    CONSTRAINT [FK_tblUserExercise_tblUser] FOREIGN KEY ([userEmail]) REFERENCES [tblUser]([userEmail])
)
