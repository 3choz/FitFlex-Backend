# Class that defines the Password object. Object will match values of the table: tblUser

from DBConnect import DBAction,DBQuery

class User:

    def __init__(self):
        pass
    # Contructor
    def __init__(self, userEmail, passID, prgmID, userFirstName, userLastName, userDOB, userPhone, userSex):
        self.userEmail = userEmail
        self.passID = passID
        self.prgmID = prgmID
        self.userFirstName = userFirstName
        self.userLastName = userLastName
        self.userDOB = userDOB
        self.userPhone = userPhone
        self.userSex = userSex

    # Create record in the database.
    def create(self):
        print("tbd")

    # Update record in the database.
    def update(self):
        print("tbd")

    # Delete record in the database.
    def delete(self):
        print("tbd")
