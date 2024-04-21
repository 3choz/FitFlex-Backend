CREATE PROCEDURE [dbo].[spUserDelete]
	@Email varchar(75)
AS
	DELETE FROM tblUserWeight WHERE userEmail = @Email;
	DECLARE @passID AS INT
	SELECT @passID = passID from tblUser WHERE userEmail = @Email;
	DELETE FROM tblPassword WHERE passID = @passID
	DELETE FROM tblUserExercise WHERE userEmail = @Email
	DELETE FROM tblUser WHERE userEmail = @Email