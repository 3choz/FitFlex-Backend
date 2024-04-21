# Class that defines the Program object. Object will match values of the table: tblProgram

from DBConnect import DBAction,DBQuery

class ProgramExercise:

    # Contructor
    def __init__(self, prgmName, prgmDescription):
        self.prgmName = prgmName
        self.prgmDescription = prgmDescription

    # Create record in the database.
    def create(self):
        print("tbd")

    # Update record in the database.
    def update(self):
        print("tbd")

    # Delete record in the database.
    def delete(self):
        print("tbd")