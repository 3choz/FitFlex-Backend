CREATE TABLE [dbo].[tblUser]
(
	[userEmail] VARCHAR(75) NOT NULL PRIMARY KEY, 
    [passID] INT NOT NULL, 
    [prgmID] INT NULL, 
    [userFirstName] VARCHAR(50) NOT NULL, 
    [userLastName] VARCHAR(50) NOT NULL, 
    [userDOB] DATE NOT NULL, 
    [userphone] VARCHAR(15) NOT NULL, 
    [userSex] VARCHAR(6) NULL, 
    CONSTRAINT [FK_tblUser_TotblPassword] FOREIGN KEY ([passID]) REFERENCES [tblPassword]([passID]),
    CONSTRAINT [FK_tblUser_TotblProgram] FOREIGN KEY ([prgmID]) REFERENCES [tblProgram]([prgmID])
)
