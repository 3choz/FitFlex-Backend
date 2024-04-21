CREATE PROCEDURE [dbo].[spUserExerciseDelete]
	@ID int
AS
	DELETE FROM tblUserExercise WHERE exID = @ID;