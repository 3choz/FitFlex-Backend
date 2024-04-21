CREATE PROCEDURE [dbo].[spSetUserProgram]
	@Email varchar(75),
	@ID int
AS
	DELETE FROM tblUserExercise WHERE userEmail = @Email;

	UPDATE tblUser
	SET prgmID = @ID
	WHERE userEmail = @Email;