# Class that defines the exercise object. Object will match values of the table: tblExercise

from DBConnect import DBAction,DBQuery

class Exercise:

    # Contructor
    def __init__(self, exID, exName, exDescription, exTrainerSex, exVideoLength, exVideoLink):
        self.exID = exID
        self.exName = exName
        self.exDescription = exDescription
        self.exTrainerSex = exTrainerSex
        self.exVideoLength = exVideoLength
        self.exVideoLink = exVideoLink

    # Create record in the database.
    def create(self):
        DBAction("Exec spExerciseInsert @Name='"+self.exName+"', @Description='"+self.exDescription+"', @VideoLink='"+self.exVideoLink+"', @TrainerSex='"+self.exTrainerSex+"', @VideoLength='"+self.exVideoLength+"'")
        tempid = DBQuery("select * from tblExercise where exName='"+ self.exName + "' and exDescription ='" + self.exDescription +"'")
        self.exID = int(tempid[0])

    # Update record in the database.
    def update(self,exName, exDescription, exTrainerSex, exVideoLength, exVideoLink):
        self.exName = exName
        self.exDescription = exDescription
        self.exTrainerSex = exTrainerSex
        self.exVideoLength = exVideoLength
        self.exVideoLink = exVideoLink
        DBAction("Exec spExerciseUpdate @ID='" + self.exID + "', @Name='"+exName+"', @Description='"+exDescription+"', @VideoLink='"+exVideoLink+"', @TrainerSex='"+exTrainerSex+"', @VideoLength='"+exVideoLength+"'")

    # Delete record in the database.
    def delete(self):
        DBAction("Exec spExerciseDelete @ID='"+self.exID+"'")