CREATE PROCEDURE [dbo].[spGetWeight]
	@ID int
AS
	SELECT * from tblUserWeight uw where uw.uwID = @ID 