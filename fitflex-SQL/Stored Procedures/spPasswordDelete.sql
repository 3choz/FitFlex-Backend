CREATE PROCEDURE [dbo].[spPasswordDelete]
	@ID int
AS
	DELETE FROM tblPassword WHERE passID = @ID