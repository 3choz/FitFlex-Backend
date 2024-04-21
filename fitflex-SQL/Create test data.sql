--DELETE FROM tblExercise
--DELETE FROM tblPassword
--DELETE FROM tblProgram
--DELETE FROM tblProgramExerciseJunc
--DELETE FROM tblUser
--DELETE FROM tblUserExercise
--DELETE FROM tblExercise
--DELETE FROM tblUserWeight

-- Create Program.
exec spProgramInsert @Name ='SwolPlus', @Description='Program to get SWOL'
DECLARE @NewPRGMID AS INT
SELECT @NewPRGMID = prgmID from tblProgram WHERE prgmName = 'SwolPlus'

-- Create exercise for the program.
exec spExerciseInsert @name='Push',@description='Push',@TrainerSex ='Male', @VideoLength=156, @Videolink='ahaiushdiuahsd'
DECLARE @NewEXID AS INT
SELECT @NewEXID = exID from tblExercise WHERE exName = 'Push'

-- Link the exercise to the program
exec spProgramExerciseInsert @exID = @NewEXID, @prgmID = @NewPRGMID

-- Create password for new user, Set the salt and hash to something unique. Get the password ID that you just made. Auto increment is enabled on the password table.
exec spPasswordInsert @Salt='siuhfoihdfdeyh45yhgjkadef7ysdfsdfs',@Hash='(UHAofyhahfa987eyf83hnkrjhifgeh';
DECLARE @NewPasswordID AS INT
SELECT @NewPasswordID = passID from tblPassword WHERE passSalt = 'siuhfoihdfdeyh45yhgjkadef7ysdfsdfs' and passHash = '(UHAofyhahfa987eyf83hnkrjhifgeh';

-- Create new user. Email needs to be something unique or it will fail as the email is the primary key.
exec spUserInsert @Email='joker@jokes.com', @passID=@NewPasswordID, @First='Joker', @Last = 'Jokerson', @DOB = '02/05/1970' , @phone='1234567898', @Sex = 'Male'

-- Set Users program, sets the program of a user. 
DECLARE @tempPRGMID AS INT
exec spSetUserProgram @email='joker@jokes.com', @ID=@NewPRGMID

-- Create User weight, set email to be same email as new user
exec spWeightInsert @Email='joker@jokes.com',@Date='02/02/2024',@Weight=120.00
exec spWeightInsert @Email='joker@jokes.com',@Date='03/02/2024',@Weight=130.00
exec spWeightInsert @Email='joker@jokes.com',@Date='04/02/2024',@Weight=140.00

-- Create an exercise record for the user
exec spUserExerciseInsert @exID = @NewEXID, @email = 'joker@jokes.com', @date = '04/02/2024', @Type = 'Reps', @amount = 2