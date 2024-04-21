CREATE PROCEDURE [dbo].[spProgramExerciseInsert]
	@exID int,
	@prgmID int
AS
	INSERT INTO tblProgramExerciseJunc
	VALUES(@exID,@prgmID)