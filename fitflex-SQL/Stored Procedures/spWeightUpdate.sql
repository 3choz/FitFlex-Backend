CREATE PROCEDURE [dbo].[spWeightUpdate]
	@ID int,
	@Date date,
	@Weight decimal(18,2)
AS
	UPDATE tblUserWeight
	SET uwDate = @Date, uwWeight = @Weight
	WHERE uwID = @ID;