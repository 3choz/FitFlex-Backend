CREATE PROCEDURE [dbo].[spGetExercise]
	@ID int
AS
	select * from tblExercise ex where ex.exID = @ID