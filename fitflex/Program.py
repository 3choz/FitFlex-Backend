# Class that defines the Program object. Object will match values of the table: tblProgram

from fitflex.DBConnect import DBAction,DBQuery

class Program:

    # Contructor
    def __init__(self, prgmName, prgmDescription):
        self.prgmName = prgmName
        self.prgmDescription = prgmDescription

    # Create record in the database.
    def create(self):
        DBAction("")

    # Update record in the database.
    def update(self):
        DBAction("")

    # Delete record in the database.
    def delete(self):
        DBAction("")