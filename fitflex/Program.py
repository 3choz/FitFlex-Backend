# Class that defines the Program object. Object will match values of the table: tblProgram

from fitflex.DBConnect import DBAction,DBQuery

class Program:

    # Contructor
    def __init__(self, prgmName, prgmDescription):
        self.prgmName = prgmName
        self.prgmDescription = prgmDescription
        

    # Create record in the database.
    def create(self):
        DBAction("Exce spProgramInsert @Name='"+self.prgmName+"', @Description='"+self.prgmDescription+"', @Difficulty='"+self.prgmDifficulty+"'")

    # Update record in the database.
    def update(self, prgmName, prgmDescription):
        self.prgmName = prgmName
        self.prgmDescription = prgmDescription
        DBAction("Exce spProgram @ID='"+self.prgmID+"', @Name='"+self.prgmName+"', @Description='"+self.prgmDescription+"', @Difficulty='"+self.prgmDifficulty+"'")

    # Delete record in the database.
    def delete(self):
        DBAction("Exec spProgramDelete @ID='"+self.prgmID+"'")
