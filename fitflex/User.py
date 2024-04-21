# Class that defines the Password object. Object will match values of the table: tblUser

from fitflex.DBConnect import DBAction, DBQuery

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
        if(DBAction("EXEC spUserInsert @Email='"+ self.userEmail +"', @passID='"+str(self.passID)+"', @First='"+ self.userFirstName +"', @Last='"+self.userLastName+"', @DOB='"+self.userDOB+"', @Phone ='"+self.userPhone+"', @sex='"+ self.userSex + "'") == False):
            DBAction("Delete from tblpassword where @passID='"+str(self.passID)+"'")
            return False
        return True

    # Update record in the database.
    def update(self, userFirstName, userLastName, userDOB, userPhone, userSex):
        DBAction("EXEC spUserUpdate @Email='"+self.userEmail+"', @First='"+ userFirstName +"', @Last='" + userLastName+"', @DOB='" + userDOB+"', @Phone ='"+ userPhone+"', @sex='"+ userSex + "'")

    # Delete record in the database.
    def delete(self):
        DBAction("EXEC spUserDelete @Email='"+ self.userEmail +"'")
