CREATE PROCEDURE [dbo].[spGetUserExercises]
	@Email varchar(75),
	@ID int
AS
	SELECT * from tblUserExercise ue where ue.userEmail = @Email and ue.exID = @ID