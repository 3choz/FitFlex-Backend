# Class that defines the UserWeight object. Object will match values of the table: tblUserWeight

from DBConnect import DBAction,DBQuery

class UserWeight:

    # Contructor
    def __init__(self,uwID,userEmail,uwDate,uwWeight):
        self.uwID = uwID
        self.userEmail = userEmail
        self.uwDate = uwDate
        self.uwWeight = uwWeight

    # Create record in the database.
    def create(self):
        print("tbd")

    # Update record in the database.
    def update(self):
        print("tbd")

    # Delete record in the database.
    def delete(self):
        print("tbd")