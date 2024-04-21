CREATE PROCEDURE [dbo].[spPasswordInsert]
	@Salt varchar(255),
	@Hash varchar(255)
AS
	INSERT INTO tblPassword
	VALUES(@Salt,@Hash);