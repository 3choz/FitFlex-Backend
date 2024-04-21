CREATE PROCEDURE [dbo].[spExerciseInsert]
	@Name varchar(75),
	@Description varchar(255),
	@VideoLink varchar(255),
	@TrainerSex varchar(6),
	@VideoLength int
AS
	INSERT INTO tblExercise
	VALUES(@Name,@Description,@VideoLink,@TrainerSex,@VideoLength);
