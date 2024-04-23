CREATE PROCEDURE [dbo].[spGetProgram]
	@Email varchar(255)
AS
	select p.prgmID,p.prgmName,p.prgmDescription,p.prgmDifficulty from tblProgram p
	join tblUser u on p.prgmID = u.prgmID
	where u.userEmail = @Email;