CREATE PROCEDURE [dbo].[spDeleteExercise]
	@ID int
AS
	DELETE FROM tblExercise WHERE exID = @ID