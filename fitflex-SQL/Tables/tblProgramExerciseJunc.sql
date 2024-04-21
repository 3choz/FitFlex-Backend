CREATE TABLE [dbo].[tblProgramExerciseJunc]
(
	[exID] INT NOT NULL, 
    [prgmID] INT NOT NULL,
	CONSTRAINT PK_Program_Exercise PRIMARY KEY (exID,prgmID), 
    CONSTRAINT [FK_tblProgramExerciseJunc_TotblExercise] FOREIGN KEY ([exID]) REFERENCES [tblExercise]([exID]),
	CONSTRAINT [FK_tblProgramExerciseJunc_TotblProgram] FOREIGN KEY ([prgmID]) REFERENCES [tblProgram]([prgmID])
)
