CREATE PROCEDURE [dbo].[spGetUser]
	@Email varchar(75)
AS
	select * from tblUser u where u.userEmail = @Email