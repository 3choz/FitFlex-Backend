CREATE PROCEDURE [dbo].[spUserInsert]
	@Email varchar(75),
	@passID int,
	@First varchar(50),
	@Last varchar(50),
	@DOB date,
	@Phone varchar(15),
	@Sex varchar(6)
AS
	INSERT INTO tblUser
	VALUES(@Email,@passID,NULL,@First,@Last,@DOB,@Phone,@Sex)