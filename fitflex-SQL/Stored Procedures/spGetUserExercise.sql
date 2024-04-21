CREATE PROCEDURE [dbo].[spGetUserExercise]
	@ID int
AS
	SELECT * from tblUserExercise ue where ue.ueID = @ID