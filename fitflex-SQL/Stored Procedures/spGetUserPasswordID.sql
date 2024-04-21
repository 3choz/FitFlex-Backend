CREATE PROCEDURE [dbo].[spGetUserPasswordID]
	@EMAIL varchar(75)
AS
	select p.passID, p.passSalt from tblUser u
	join tblPassword p on u.passID = p.passID
	where u.userEmail = @EMAIL
