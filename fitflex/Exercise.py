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
        print("tbd")

    # Update record in the database.
    def update(self):
        print("tbd")

    # Delete record in the database.
    def delete(self):
        print("tbd")