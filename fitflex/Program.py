# Class that defines the Program object. Object will match values of the table: tblProgram

from fitflex.DBConnect import DBAction,DBQuery

class Program:

    # Contructor
    def __init__(self, prgmID, prgmName, prgmDescription, prgmDifficulty):
        self.prgmID = prgmID
        self.prgmName = prgmName
        self.prgmDescription = prgmDescription
        self.prgmDifficulty = prgmDifficulty

    # Create record in the database.
    def create(self):
        DBAction("Exec spProgramInsert @Name='"+self.prgmName+"', @Description='"+self.prgmDescription+"', @Difficulty='"+self.prgmDifficulty+"'")

    # Update record in the database.
    def update(self,prgmID, prgmName, prgmDescription, prgmDifficulty):
        self.prgmID = prgmID
        self.prgmName = prgmName
        self.prgmDescription = prgmDescription
        self.prgmDifficulty = prgmDifficulty

        if (DBAction("Exec spProgramUpdate @ID='"+str(self.prgmID)+"', @Name='"+self.prgmName+"', @Description='"+self.prgmDescription+"', @Difficulty='"+self.prgmDifficulty+"'")):
            return True
        return False

    # Delete record in the database.
    def delete(self):
        DBAction("Exec spProgramDelete @ID='"+self.prgmID+"'")
