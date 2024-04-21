CREATE PROCEDURE [dbo].[spProgramInsert]
	@Name varchar(255),
	@Description varchar(255)
AS
	INSERT INTO tblProgram
	VALUES(@Name,@Description)