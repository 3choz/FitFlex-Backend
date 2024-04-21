# Class that defines the Program object. Object will match values of the table: tblUserExercise

from DBConnect import DBAction,DBQuery

class UserExercise:

    # Contructor
    def __init__(self,ueID,exID,userEmail,ueDate,euType,ueAmount):
        self.ueID = ueID
        self.exID = exID
        self.userEmail = userEmail
        self.ueDate = ueDate
        self.euType = euType
        self.ueAmount = ueAmount

    # Create record in the database.
    def create(self):
        print("tbd")

    # Update record in the database.
    def update(self):
        print("tbd")

    # Delete record in the database.
    def delete(self):
        print("tbd")
