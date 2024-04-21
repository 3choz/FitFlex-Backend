CREATE PROCEDURE [dbo].[spUserUpdate]
	@Email varchar(75),
	@First varchar(50),
	@Last varchar(50),
	@DOB date,
	@Phone varchar(15),
	@Sex varchar(6)
AS
	UPDATE tblUser
	SET userFirstName = @First, userLastName = @Last, userDOB = @DOB, userphone = @Phone, userSex = @Sex
	WHERE userEmail = @Email;