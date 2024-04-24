# Class that defines the Password object. Object will match values of the table: tblPassword

import hashlib
import string
import random

from fitflex.DBConnect import DBAction,DBQuery

class Password:

    # Returns True or False
    def login(self, email, password):

        # Get password hash and salt
        hashSalt = DBQuery("exec spGetPasswordHash @email ='"+email+"'")
        try:
            if(len(hashSalt[0])>3):
                output = (hashSalt[0])[2:len(hashSalt[0])-2]
                output = output.split("', '")
                temphash = output[0]
                tempsalt = output[1]

                # Generate password
                generatedPassword = hashlib.sha256((password+tempsalt).encode("utf-8")).hexdigest()

                #Compare passwords
                if temphash == generatedPassword:
                    return True
                return False
            print("error")
        except:
            return False

    #create password. This is only called during user creation.
    def create(self, password):

        # create Salt
        salt = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=25))
        # create Hash
        passhash = hashlib.sha256((password+salt).encode("utf-8"))
        DBAction("EXEC spPasswordInsert @Salt='"+ salt +"', @Hash='"+ passhash.hexdigest() + "'")

        tempstr = DBQuery("select passID from tblPassword where passSalt = '"+ salt +"' and passHash='"+ passhash.hexdigest() +"'")[0]
        passid = int(tempstr[1:len(tempstr)-2])
        return passid

    # Update Password. Password reset.
def update(self, currentPassword, newPassword):
    # Fetch current password hash and salt from the database
    hashSalt = DBQuery("exec spGetPasswordHash @Email = '"+ self.userEmail +"'")
    if hashSalt:
        currentHash = hashSalt[0].get('passHash')
        currentSalt = hashSalt[0].get('passSalt')

        # Check if the current password matches the provided currentPassword
        if hashlib.sha256((currentPassword + currentSalt).encode("utf-8")).hexdigest() == currentHash:
            # Generate new salt and hash for the newPassword
            newSalt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
            newHash = hashlib.sha256((newPassword + newSalt).encode("utf-8")).hexdigest()
            
            # Update the password in the database with the new salt and hash
            DBAction("EXEC spPasswordUpdate @ID='"+ str(self.passID) +"', @NewSalt='"+ newSalt +"', @NewHash='"+ newHash + "'")
            return True
        else:
            # Current password does not match
            return False
    else:
        # Error fetching current password hash and salt
        return False

