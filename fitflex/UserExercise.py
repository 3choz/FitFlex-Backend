# Class that defines the Program object. Object will match values of the table: tblUserExercise

from fitflex.DBConnect import DBAction,DBQuery

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
        DBAction("Exce spUserExerciseInsert @exID='"+self.exID+"', @Email='"+self.userEmail+"', @Date='"+self.ueDate+"', @Type='"+self.euType+"', @Amount='"+self.ueAmount+"'")

    # Update record in the database.
    def update(self, ueDate, euType, ueAmount):
        self.ueDate = ueDate
        self.euType = euType
        self.ueAmount = ueAmount
        DBAction("Exce spUserExerciseUpdate @exID='"+self.ueID+"', @Date='"+self.ueDate+"', @Type='"+self.euType+"', @Amount='"+self.ueAmount+"'")

    # Delete record in the database.
    def delete(self):
        DBAction("Exec spExerciseDelete @ID='"+self.exID+"'")
