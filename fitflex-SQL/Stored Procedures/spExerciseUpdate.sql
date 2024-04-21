CREATE PROCEDURE [dbo].[spExerciseUpdate]
	@ID int,
	@Name varchar(75),
	@Description varchar(255),
	@TrainerSex varchar(6),
	@VideoLength int,
	@VideoLink varchar(255)
AS
	UPDATE tblExercise
	SET exName = @Name, exDescription = @Description, exTrainerSex = @TrainerSex, exVideoLength = @VideoLength,exVideoLink = @VideoLink
	WHERE exID = @ID;