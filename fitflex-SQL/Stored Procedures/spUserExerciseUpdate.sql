CREATE PROCEDURE [dbo].[spUserExerciseUpdate]
	@ID int,
	@Date date,
	@Type varchar(75),
	@Amount decimal(18,2)
AS
	UPDATE tblUserExercise
	SET ueDate = @Date, ueType = @Type, ueAmount = @Amount
	WHERE ueID = @ID;