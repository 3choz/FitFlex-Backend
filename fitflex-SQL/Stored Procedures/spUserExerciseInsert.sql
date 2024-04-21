CREATE PROCEDURE [dbo].[spUserExerciseInsert]
	@exID int,
	@Email varchar(75),
	@Date date,
	@Type varchar(75),
	@Amount decimal(18,2)
AS
	INSERT INTO tblUserExercise
	VALUES(@exID,@Email,@Date,@Type,@Amount);
