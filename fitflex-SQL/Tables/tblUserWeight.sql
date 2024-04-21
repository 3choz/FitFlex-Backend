CREATE TABLE [dbo].[tblUserWeight]
(
	[uwID] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [userEmail] VARCHAR(75) NOT NULL, 
    [uwDate] NCHAR(10) NOT NULL, 
    [uwWeight] DECIMAL(18, 2) NOT NULL, 
    CONSTRAINT [FK_tblUserWeight_TotblUser] FOREIGN KEY ([userEmail]) REFERENCES [tblUser]([userEmail])
)
