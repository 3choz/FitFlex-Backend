# Class that defines the Program object. Object will match values of the table: tblUserExercise

from fitflex.DBConnect import DBAction

class UserExercise:

    # Contructor
    def __init__(self,ueID,exID,userEmail,ueDate,euType,ueAmount):
        self.ueID = ueID
        self.exID = exID
        self.userEmail = userEmail
        self.ueDate = ueDate
        self.ueType = euType
        self.ueAmount = ueAmount

    # Create record in the database.
    def create(self):
        if DBAction("Exec spUserExerciseInsert @exID='" + str(self.exID)+"', @Email='"+self.userEmail+"', @Date='"+self.ueDate +"', @Type='"+self.ueType +"', @Amount='" + str(self.ueAmount) + "'") == True:
            return True
        return False

    # Update record in the database.
    def update(self, ueDate, ueType, ueAmount):
        self.ueDate = ueDate
        self.ueType = ueType
        self.ueAmount = ueAmount
        if (DBAction("Exec spUserExerciseUpdate @ID="+str(self.ueID) + ", @Date='"+self.ueDate+"', @Type='"+self.ueType+"', @Amount="+str(self.ueAmount))):
            return True
        return False

    # Delete record in the database.
    def delete(self):
        #if(DBAction("Exec spExerciseDelete @ID='"+ str(self.ueID) +"'")):
        return True
        #return False
