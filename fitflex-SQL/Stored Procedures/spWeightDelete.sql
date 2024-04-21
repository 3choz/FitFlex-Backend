CREATE PROCEDURE [dbo].[spWeightDelete]
	@ID int = 0
AS
	DELETE FROM tblUserWeight WHERE uwID = @ID;