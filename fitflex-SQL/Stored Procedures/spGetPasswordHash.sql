CREATE PROCEDURE [dbo].[spGetPasswordHash]
	@EMAIL varchar(75)
AS
	select p.passHash from tblUser u
	join tblPassword p on u.passID = p.passID
	where u.userEmail = @EMAIL;
