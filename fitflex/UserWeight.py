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
        DBAction("Exce spWeightInsert  @Email='"+self.userEmail+"', @Date='"+self.uwDate+"', @Weight='"+self.uwWeight+"'")

    # Update record in the database.
    def update(self, uwDate,uwWeight):
        self.uwDate = uwDate
        self.uwWeight = uwWeight
        DBAction("Exec spExerciseUpdate @ID='" + self.uwID + "', @Date='"+self.uwDate+"', @Weight='"+self.uwWeight+"' ")

    # Delete record in the database.
    def delete(self):
        DBAction("Exec spExerciseDelete @ID='"+self.uwID+"'")