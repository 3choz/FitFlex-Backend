CREATE PROCEDURE [dbo].[spPasswordUpdate]
	@ID int,
	@Salt varchar(255),
	@Hash varchar(255)
AS
	UPDATE tblPassword
	SET passHash = @Hash, passSalt = @Salt
	WHERE passID = @ID;