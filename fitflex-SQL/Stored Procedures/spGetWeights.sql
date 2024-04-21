CREATE PROCEDURE [dbo].[spGetWeights]
	@Email varchar(75)
AS
	SELECT * from tblUserWeight uw where uw.userEmail = @Email