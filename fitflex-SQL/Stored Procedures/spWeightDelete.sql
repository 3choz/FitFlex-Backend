CREATE PROCEDURE [dbo].[spWeightDelete]
	@ID int
AS
	DELETE FROM tblUserWeight WHERE uwID = @ID;