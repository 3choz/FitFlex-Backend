# Class Responsible for connecting to the database. 

import pypyodbc as obdc

#global variable declaration
maxAttempts = 9

# Peform DB actions (create, update, delete). Returns true or false if the action was performed.
def DBAction(SQLStatement):
    
    # Database Connection Information
    connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:cmsc495-capstone-db-server.database.windows.net,1433;Database=CapstoneDB;Uid=cmsc495;Pwd=Capstone495;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    currentAttempt = 0
    
    # Database Connection
    while True:
        try:
            currentAttempt = currentAttempt + 1
            if (currentAttempt > maxAttempts):
                    return False
            conn = obdc.connect(connection_string)

            # Connect to DB and excute statement
            cursor = conn.cursor()
            cursor.execute(SQLStatement)
            cursor.commit()

            break
        except:
            print('Failed Attempt')
    return True

# Retrieve DB Query (SQLStatement). Returns Cursor Object
def DBQuery(SQLStatement):

    # Database Connection Information
    connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:cmsc495-capstone-db-server.database.windows.net,1433;Database=CapstoneDB;Uid=cmsc495;Pwd=Capstone495;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    currentAttempt = 0

    # Database Connection
    while True:
        try:
            currentAttempt = currentAttempt + 1
            if (currentAttempt > maxAttempts):
                    return "Failed"
            conn = obdc.connect(connection_string)

            # Connect to DB and excute statement
            cursor = conn.cursor()
            cursor.execute(SQLStatement)
            
            # Create array and get rows
            rows = []
            for x in cursor:
                rows.append(str(x))
            return rows
        except:
            print('Failed Attempt')