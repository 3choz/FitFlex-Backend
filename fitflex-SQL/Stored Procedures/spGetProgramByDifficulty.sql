CREATE PROCEDURE [dbo].[spGetProgramByDifficulty]
	@Difficulty varchar(255)
AS
	select * from tblProgram 
	where prgmDifficulty = @Difficulty;