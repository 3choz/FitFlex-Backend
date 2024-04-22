CREATE PROCEDURE [dbo].[spProgramUpdate]
	@ID int,
	@Name varchar(255),
	@Description varchar(255),
	@Difficulty varchar(255)
AS
	UPDATE tblProgram
	SET prgmName = @Name, prgmDescription = @Description, prgmDifficulty = @Difficulty
	WHERE prgmID = @ID;