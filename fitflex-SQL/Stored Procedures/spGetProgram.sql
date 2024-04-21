CREATE PROCEDURE [dbo].[spGetProgram]
	@ID int
AS
	select * from tblProgram prgm where prgm.prgmID = @ID 