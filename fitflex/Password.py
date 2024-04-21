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
        print(salt)
        # create Hash
        passhash = hashlib.sha256((password+salt).encode("utf-8"))
        print(passhash.hexdigest())
        DBAction("EXEC spPasswordInsert @Salt='"+ salt +"', @Hash='"+ passhash.hexdigest() + "'")
        
    # Update Password. Password reset.
    def update(self, currentPassword, newPassword):
        print("tbd")

    # delete password. This is only called during user deletion.
    def delete(self, userEmail):
        print("delete")