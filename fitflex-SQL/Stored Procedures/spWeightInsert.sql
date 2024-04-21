CREATE PROCEDURE [dbo].[spWeightInsert]
	@Email varchar(75),
	@Date date,
	@Weight decimal(18,2)
AS
	INSERT INTO tblUserWeight
	VALUES(@Email,@Date,@Weight)