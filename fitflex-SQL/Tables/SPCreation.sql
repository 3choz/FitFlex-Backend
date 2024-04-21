CREATE PROCEDURE [dbo].[spDeleteExercise]
	@ID int
AS
	DELETE FROM tblExercise WHERE exID = @ID;

CREATE PROCEDURE [dbo].[spExerciseInsert]
	@Name varchar(75),
	@Description varchar(255),
	@TrainerSex varchar(255),
	@VideoLength varchar(6),
	@VideoLink time(7)
AS
	INSERT INTO tblExercise
	VALUES(@Name,@Description,@TrainerSex,@VideoLength,@VideoLink);

CREATE PROCEDURE [dbo].[spExerciseUpdate]
	@ID int,
	@Name varchar(75),
	@Description varchar(255),
	@TrainerSex varchar(255),
	@VideoLength varchar(6),
	@VideoLink time(7)
AS
	UPDATE tblExercise
	SET exName = @Name, exDescription = @Description, exTrainerSex = @TrainerSex, exVideoLength = @VideoLength,exVideoLink = @VideoLink
	WHERE exID = @ID;

CREATE PROCEDURE [dbo].[spGetExercise]
	@ID int
AS
	select * from tblExercise ex where ex.exID = @ID;

CREATE PROCEDURE [dbo].[spGetExercises]
AS
	select * from tblExercise;

CREATE PROCEDURE [dbo].[spGetPasswordHash]
	@ID int
AS
	select p.passHash from tblPassword p where passID = @ID;

CREATE PROCEDURE [dbo].[spGetProgram]
	@ID int
AS
	select * from tblProgram prgm where prgm.prgmID = @ID ;

CREATE PROCEDURE [dbo].[spGetPrograms]
AS
	select * from tblProgram;

CREATE PROCEDURE [dbo].[spGetUser]
	@Email varchar(75)
AS
	select * from tblUser u where u.userEmail = @Email;

CREATE PROCEDURE [dbo].[spGetUserExercise]
	@ID int
AS
	SELECT * from tblUserExercise ue where ue.ueID = @ID;

CREATE PROCEDURE [dbo].[spGetUserExercises]
	@Email varchar(75),
	@ID int
AS
	SELECT * from tblUserExercise ue where ue.userEmail = @Email and ue.exID = @ID;

CREATE PROCEDURE [dbo].[spGetWeight]
	@ID int
AS
	SELECT * from tblUserWeight uw where uw.uwID = @ID ;

CREATE PROCEDURE [dbo].[spGetWeights]
	@Email varchar(75)
AS
	SELECT * from tblUserWeight uw where uw.userEmail = @Email;

CREATE PROCEDURE [dbo].[spPasswordDelete]
	@ID int
AS
	DELETE FROM tblPassword WHERE passID = @ID;

CREATE PROCEDURE [dbo].[spPasswordInsert]
	@Salt varchar(255),
	@Hash varchar(255)
AS
	INSERT INTO tblPassword
	VALUES(@Salt,@Hash);

CREATE PROCEDURE [dbo].[spPasswordLogin]
	@ID int,
	@Hash varchar(255)
AS
	IF EXISTS(select * from tblPassword where passID = @ID and passHash = @Hash)
		Select 'True'
	ELSE
		Select 'False';

CREATE PROCEDURE [dbo].[spPasswordUpdate]
	@ID int,
	@Salt varchar(255),
	@Hash varchar(255)
AS
	UPDATE tblPassword
	SET passHash = @Hash, passSalt = @Salt
	WHERE passID = @ID;

CREATE PROCEDURE [dbo].[spProgramDelete]
	@ID int
AS
	DELETE FROM tblProgram WHERE prgmID = @ID;

CREATE PROCEDURE [dbo].[spProgramExerciseDelete]
	@exID int,
	@prgrm int
AS
	DELETE FROM tblProgramExerciseJunc WHERE exID = @exID AND prgmID = @prgrm;

CREATE PROCEDURE [dbo].[spProgramExerciseInsert]
	@exID int,
	@prgmID int
AS
	INSERT INTO tblProgramExerciseJunc
	VALUES(@exID,@prgmID);

CREATE PROCEDURE [dbo].[spProgramInsert]
	@Name varchar(255),
	@Description varchar(255)
AS
	INSERT INTO tblProgram
	VALUES(@Name,@Description);

CREATE PROCEDURE [dbo].[spProgramUpdate]
	@ID int,
	@Name varchar(255),
	@Description varchar(255)
AS
	UPDATE tblProgram
	SET prgmName = @Name, prgmDescription = @Description
	WHERE prgmID = @ID;

CREATE PROCEDURE [dbo].[spSetUserProgram]
	@Email varchar(75),
	@ID int
AS
	DELETE FROM tblUserExercise WHERE userEmail = @Email;

	UPDATE tblUser
	SET prgmID = @ID
	WHERE userEmail = @Email;

CREATE PROCEDURE [dbo].[spUserDelete]
	@Email varchar(75)
AS
	DELETE FROM tblUserWeight WHERE userEmail = @Email;
	DECLARE @passID AS INT
	SELECT @passID = passID from tblUser WHERE userEmail = @Email;
	DELETE FROM tblPassword WHERE passID = @passID
	DELETE FROM tblUserExercise WHERE userEmail = @Email
	DELETE FROM tblUser WHERE userEmail = @Email;

CREATE PROCEDURE [dbo].[spUserExerciseDelete]
	@ID int
AS
	DELETE FROM tblUserExercise WHERE ueDate = @ID;

CREATE PROCEDURE [dbo].[spUserExerciseInsert]
	@exID int,
	@Email varchar(75),
	@Date date,
	@Type varchar(75),
	@Amount decimal(18,2)
AS
	INSERT INTO tblUserExercise
	VALUES(@exID,@Email,@Date,@Type,@Amount);

CREATE PROCEDURE [dbo].[spUserExerciseUpdate]
	@ID int,
	@Date date,
	@Type varchar(75),
	@Amount decimal(18,2)
AS
	UPDATE tblUserExercise
	SET ueDate = @Date, ueType = @Type, ueAmount = @Amount
	WHERE ueID = @ID;

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
	VALUES(@Email,@passID,NULL,@First,@Last,@DOB,@Phone,@Sex);

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

CREATE PROCEDURE [dbo].[spWeightDelete]
	@ID int = 0
AS
	DELETE FROM tblUserWeight WHERE uwID = @ID;

CREATE PROCEDURE [dbo].[spWeightInsert]
	@Email varchar(75),
	@Date date,
	@Weight decimal(18,2)
AS
	INSERT INTO tblUserWeight
	VALUES(@Email,@Date,@Weight);

CREATE PROCEDURE [dbo].[spWeightUpdate]
	@ID int,
	@Date date,
	@Weight decimal(18,2)
AS
	UPDATE tblUserWeight
	SET uwDate = @Date, uwWeight = @Weight
	WHERE uwID = @ID;