CREATE PROCEDURE [dbo].[spProgramExerciseDelete]
	@exID int,
	@prgrm int
AS
	DELETE FROM tblProgramExerciseJunc WHERE exID = @exID AND prgmID = @prgrm;