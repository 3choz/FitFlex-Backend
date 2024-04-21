CREATE PROCEDURE [dbo].[spProgramDelete]
	@ID int
AS
	DELETE FROM tblProgram WHERE prgmID = @ID;