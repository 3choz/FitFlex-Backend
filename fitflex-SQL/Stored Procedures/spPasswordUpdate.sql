CREATE PROCEDURE [dbo].[spPasswordUpdate]
	@Email varchar(255),
	@Salt varchar(255),
	@Hash varchar(255)
AS
	DECLARE @tempPassID AS INT
	select @tempPassID = passID from tbluser where userEmail = @Email;

	UPDATE tblPassword
	SET passHash = @Hash, passSalt = @Salt
	WHERE passID = @tempPassID;