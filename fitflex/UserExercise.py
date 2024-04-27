# Class that defines the Program object. Object will match values of the table: tblUserExercise

from fitflex.DBConnect import DBAction

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
        if DBAction("Exce spUserExerciseInsert @exID='"+self.exID+"', @Email='"+self.userEmail+"', @Date='"+self.ueDate+"', @Type='"+self.euType+"', @Amount='"+self.ueAmount+"'") == True:
            return True
        return False

    # Update record in the database.
    def update(self,ueID, ueDate, euType, ueAmount):
        self.ueID = ueID
        self.ueDate = ueDate
        self.euType = euType
        self.ueAmount = ueAmount
        if (DBAction("Exce spUserExerciseUpdate @exID='"+self.ueID+"', @Date='"+self.ueDate+"', @Type='"+self.euType+"', @Amount='"+self.ueAmount+"'")):
            return True
        return False

    # Delete record in the database.
    def delete(self):
        if(DBAction("Exec spExerciseDelete @ID='"+self.ueID+"'")):
            return True
        return False
