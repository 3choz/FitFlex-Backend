CREATE PROCEDURE [dbo].[spGetExerciseByUserProgram]
	@Email Varchar(255)
AS
	DECLARE @tempprgmID AS INT
	select @tempprgmID = u.prgmID from tblUser u where u.userEmail = @Email;
	select * from tblProgramExerciseJunc pej 
	join tblExercise e on pej.exID = e.exID
	where pej.prgmID = @tempprgmID;