# Class that defines the UserWeight object. Object will match values of the table: tblUserWeight

from fitflex.DBConnect import DBAction,DBQuery

class UserWeight:

    # Contructor
    def __init__(self,uwID,userEmail,uwDate,uwWeight):
        self.uwID = uwID
        self.userEmail = userEmail
        self.uwDate = uwDate
        self.uwWeight = uwWeight

    # Create record in the database.
    def create(self):
        if DBAction("Exec spWeightInsert @Email='"+self.userEmail+"', @Date='"+self.uwDate+"', @Weight='"+self.uwWeight+"'") == True:
            return True
        return False

    # Update record in the database.
    def update(self,uwID, uwDate,uwWeight):
        self.uwID = uwID
        self.uwDate = uwDate
        self.uwWeight = uwWeight
        
        if DBAction("Exec spExerciseUpdate @ID='" + self.uwID + "', @Date='"+self.uwDate+"', @Weight='"+self.uwWeight+"' ") == True:
            return True
        return False

    # Delete record in the database.
    def delete(self):
        if DBAction("Exec spExerciseDelete @ID='"+self.uwID+"'") == True:
            return True
        return False