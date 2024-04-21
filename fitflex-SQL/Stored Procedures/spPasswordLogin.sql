CREATE PROCEDURE [dbo].[spPasswordLogin]
	@ID int,
	@Hash varchar(255)
AS
	IF EXISTS(select * from tblPassword where passID = @ID and passHash = @Hash)
		Select 'True'
	ELSE
		Select 'False'