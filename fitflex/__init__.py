from ast import Delete
import os
import json

from flask import (Flask, jsonify, render_template, request)
from flask_cors import CORS

from fitflex.Password import Password
from fitflex.User import User
from fitflex.Program import Program
from fitflex.UserExercise import UserExercise
from fitflex.UserWeight import UserWeight
from fitflex.DBConnect import DBAction, DBQuery


app = Flask(__name__, template_folder = os.path.abspath("./templates"), static_folder=os.path.abspath("./static"))
CORS(app) # Enable CORS for all routes

@app.route('/')

def index():
   print('Request for index page received')
   return render_template('index.html')

# API call for the logging in the user. 
# Password Login Method
@app.route('/api/login', methods=['POST'])
def login():

    userEmail = request.json['userEmail']    
    userPassword = request.json['userPassword']
    tempPass = Password()
    serialized_items=""
    try:
        if tempPass.login(userEmail,userPassword) == True:
            serialized_items = {"user logged in": True}
        else:
            serialized_items = {"user logged in": False}

    except Exception as e:
        serialized_items = {"user logged in": False,
                            "Error Message":str(e)}
    
    return jsonify(serialized_items)

# API call for creating a user. This will be called under the create account page.
@app.route('/api/createuser', methods=['POST'])
def createUser():
    try:
        userEmail = request.json['userEmail']
        userPassword = request.json['userPassword'] # This needs to be updated as this is in cleartext. BAD
        userFirstName = request.json['userFirstName']
        userLastName = request.json['userLastName']
        userDOB = request.json['userDOB']
        userPhone = request.json['userPhone']
        userSex = request.json['userSex']
        passCreation = Password()
        userPassID = passCreation.create(userPassword)
        newUser = User(userEmail,userPassID,None,userFirstName,userLastName,userDOB,userPhone,userSex)

        if newUser.create() == True:
            serialized_items = {"User Created": True}
        else:
            serialized_items = {"User Created": False}

    except Exception as e:
        serialized_items = {"User Created": False,
                            "Error Message":str(e)}

    return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

# Used for getting all Programs for program selection
@app.route('/api/getprograms', methods=['GET'])
def getPrograms():
    mylist = DBQuery("EXEC spGetPrograms")
    finaloutput="["
    for x in mylist:
        program = x.split(", ")
        finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
    finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

    return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it

# API Call for getting all Programs by difficulty for program selection
# Stored Procedure Name: "[spGetProgramByDifficulty]"
@app.route('/api/getprogramsbydifficulty', methods=['POST'])
def getProgramsByDifficulty():
    prgmDifficulty = request.json['Difficulty']

    mylist = DBQuery("EXEC spGetProgramByDifficulty @Difficulty='" + prgmDifficulty + "'")
    finaloutput="["
    if len(mylist) > 0:
        for x in mylist:
            program = x.split(", ")
            try:
                finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
            except Exception as e:
                serialized_items = {"getPrograms": False, "Error Message":str(e)}
                return jsonify(serialized_items)
        finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

        return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.
    serialized_items = {"getPrograms": False, "Message" : "No Records Found"}
    return jsonify(serialized_items) 

# API call for updating the user's program.
# Stored Procedure Name: "spSetUserProgram"
@app.route('/api/updateprogram', methods=['POST'])
def updateProgram():
    prgmID = request.json['prgmID']
    prgmName = request.json['prgmName']
    prgmDescription = request.json['prgmDescription']
    prgmDifficulty = request.json['prgmDifficulty']

    tempprogram = Program(None, None, None, None)

    if tempprogram.update(prgmID,prgmName,prgmDescription,prgmDifficulty):
        serialized_items = {"Program Updated": "True"}
    else:
        serialized_items = {"Program Updated": "False"}
    return jsonify(serialized_items)

# API call for getting the user's program.
# Stored Procedure Name: "getProgram"
@app.route('/api/getprogram', methods=['GET'])
def getProgram():
    userEmail = request.json['userEmail'] 

    mylist = DBQuery("EXEC spGetProgram @Email='" + userEmail + "'")
    finaloutput="["
    if len(mylist) > 0:
        for x in mylist:
            program = x.split(", ")
            try:
                finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
            except Exception as e:
                serialized_items = {"getPrograms": False, "Error Message":str(e)}
                return jsonify(serialized_items)
        finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

    return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

# API call for getting all exercises relating to user's program.
# Stored Procedure Name: "spGetExerciseByUserProgram" 
@app.route('/api/getuserexercise', methods=['POST'])
def getUserExercises():

    ueID = request.json['ueID'] 
    mylist = DBQuery("EXEC spgetuserexercise @ID=" + str(ueID))

    finaloutput="["
    if len(mylist) > 0:
        for x in mylist:
            program = x.split(", ")
            try:
                finaloutput = finaloutput + '{"ueID": ' + program[0][1:] + ', "exID": ' + program[1]+', "userEmail": "' + program[2][1: len(program[2])-1] + '", "ueDate": "' + program[3][14: ] +"/"+program[4]+ "/" + program[5][0:len(program[5])-1] + '", "ueType": "' + program[6][1: len(program[6])-1] + '", "ueAmount": ' + program[7][9: len(program[7])-3] +'},'
            except Exception as e:
                serialized_items = {"getExercise": False, "Error Message":str(e)}
                return jsonify(serialized_items)
        finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

        return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

# API call for getting all records relating to a user's specific exercise.
# Stored Procedure Name: "spGetUserExercises"
@app.route('/api/getuserexercises', methods=['POST'])
def getUserExercise():
    userEmail = request.json['userEmail'] 
    exID = request.json['exID'] 
    mylist = DBQuery("EXEC spgetuserexercises @Email='" + userEmail + "', @ID = " + str(exID) + "")
    finaloutput="["
    if len(mylist) > 0:
        for x in mylist:
            program = x.split(", ")
            try:
                finaloutput = finaloutput + '{"ueID": ' + program[0][1:] + ', "exID": ' + program[1]+', "userEmail": "' + program[2][1: len(program[2])-1] + '", "ueDate": "' + program[3][14: ] +"/"+program[4]+ "/" + program[5][0:len(program[5])-1] + '", "ueType": "' + program[6][1: len(program[6])-1] + '", "ueAmount": ' + program[7][9: len(program[7])-3] +'},'
            except Exception as e:
                serialized_items = {"getExercise": False, "Error Message":str(e)}
                return jsonify(serialized_items)
        finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

        return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

# API call for creating a user's exercise record.
# Stored Procedure Name: "spUserExerciseInsert"
@app.route('/api/createuserexercise', methods=['POST'])
def createUserExercise():
    try:
        exID = request.json['exID']
        userEmail = request.json['userEmail']
        ueDate = request.json['ueDate']
        euType = request.json['euType']
        ueAmount = request.json['ueAmount']
        newUserExercise = (exID, userEmail,ueDate,euType,ueAmount)

        if newUserExercise.create() == True:
            serialized_items = {"User Exercise Created": True}
        else:
            serialized_items = {"User Exercise Created": False}

    except Exception as e:
        serialized_items = {"UserExercise Created": False,
                                "Error Message":str(e)}
    return jsonify(serialized_items)

# Stored Procedure Name: "spUserExerciseUpdate"
# API call for updating a user's exercise record.
@app.route('/api/updateuserexercise', methods=['POST'])
def updateUserExercise():
        ueID = request.json['ueID']
        ueDate = request.json['ueDate']
        euType = request.json['euType']
        ueAmount = request.json['ueAmount']
        
        
        tempUserExcercise = UserExercise(None, None, None, None)

        if tempUserExcercise.update(ueID,ueDate,euType,ueAmount):
             serialized_items = {"Program Updated": "True"}
        else:
             serialized_items = {"Program Updated": "False"}
        return jsonify(serialized_items)

# Stored Procedure Name: "spUserExerciseDelete"
# TODO - API call for deleting a user's exercise record.
@app.route('/api/deleteuserexercise', methods=['POST'])
def deleteUserExercise():
         serialized_items = {"": ""}
         return jsonify(serialized_items)

# Stored Procedure Name: "spGetUser"
# API call to get user data for profile page for viewing and updating
@app.route('/api/getuser', methods=['POST'])
def getUser():
    userEmail = request.json['userEmail']
    mylist = DBQuery("EXEC spGetUser @Email='" + userEmail + "'")
    finaloutput="["
    if len(mylist) > 0:
        for x in mylist:
            program = x.split(", ")
            try:
                finaloutput = finaloutput + '{"userEmail": "' + program[0][2:len(program[0])-1] + '",'
                finaloutput = finaloutput + '"passID": ' + program[1] + ','
                finaloutput = finaloutput + '"prgmID": ' + program[2] + ','
                finaloutput = finaloutput + '"userFirstName": "' + program[3][1:len(program[3])-1] + '",'
                finaloutput = finaloutput + '"userLastName": "' + program[4][1:len(program[4])-1] + '",'
                finaloutput = finaloutput + '"UserDOB": "' + program[5][14:]
                finaloutput = finaloutput + '/' + program[6]
                finaloutput = finaloutput + '/' + program[7][0:len(program[7])-1] + '",'
                finaloutput = finaloutput + '"userPhone": "' + program[8][1:len(program[8])-1] + '",'
                finaloutput = finaloutput + '"userSex": "' + program[9][1:len(program[9])-2] +'"}'
                
            except Exception as e:
                serialized_items = {"getUser": False, "Error Message":str(e)}
                return jsonify(serialized_items)
        finaloutput=finaloutput[0:len(finaloutput)]+"]"
        print(finaloutput)

    serialized_items = {"": ""}
    return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

# API call for the updating user. It will be used under the account page.
@app.route('/api/UpdateUser', methods=['POST'])
def UpdateUser():
    try:
        userEmail = request.json['userEmail']
        userFirstName = request.json['userFirstName']
        userLastName = request.json['userLastName']
        userDOB = request.json['userDOB']
        userPhone = request.json['userPhone']
        userSex = request.json['userSex']
        updateUser = User(None,None,None,None,None,None,None,None)
        
        if updateUser.update(userEmail,userFirstName,userLastName,userDOB,userPhone,userSex) == True:
            serialized_items = {"User Updated": True}
        else:
            serialized_items = {"User Updated": False}
    except Exception as e:
        serialized_items = {"User Updated": False,
                            "Error Message":str(e)}
    return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

# API call to update password for the user.
# Stored Procedure Name: "spPasswordUpdate"
@app.route('/api/updatepassword', methods=['POST'])
def updatePassword():
    userEmail = request.json['userEmail']    
    userPassword = request.json['userPassword']
    userNewPassword = request.json['userNewPassword']

    tempPass = Password()

    try:
        if(tempPass.login(userEmail,userPassword) == True):
            if (tempPass.update(userEmail, userPassword, userNewPassword) == True):
                return jsonify({"Password Changed": True})
            else:
                return jsonify({"Password Changed": False})
    except:
        return jsonify({"Error": True})

# TODO - API call to view user weight.
# Stored Procedure Name: "spGetWeight"
@app.route('/api/getuserweight', methods=['POST'])
def getUserWeight():
    uwID = request.json['uwID']
    mylist=DBQuery("EXEC spGetweight @ID='" + uwID + "'")
    finaloutput="["
    for x in mylist:
        userWeight = x.split(", ")
        try:
            finaloutput = finaloutput + '{"uwID": ' +  userWeight[0][1:] + ', "userEmail": "' +  userWeight[1][1: len( userWeight[1])-1] + '", "uwDate": "' + userWeight[2][1: len(userWeight[2])-1]  + '", "uwWeight": "' + userWeight[3][1: len(userWeight[3])-2] +'", },'
        
        except Exception as e:
            serialized_items = {"getWeight": False, "Error Message":str(e)}
            return jsonify(serialized_items)
        
        finaloutput=finaloutput[0:len(finaloutput)]+"]"
        print(finaloutput)

# TODO - API call to view user weights.
# Stored Procedure Name: "spGetWeights"
@app.route('/api/getuserweights', methods=['POST'])
def getUserWeights():
    userEmail = request.json['userEmail']
    mylist = DBQuery("EXEC spGetWeights @Email='" + userEmail + "'")
    finaloutput="["
    for x in mylist:
        userWeights = x.split(", ")
        try:
            finaloutput = finaloutput + '{"uwID": ' +  userWeights[0][1:] + ', "userEmail": "' +  userWeights[1][1: len( userWeights[1])-1] + '", "uwDate": "' + userWeights[2][1: len(userWeights[2])-1]  + '", "uwWeight": "' + userWeights[3][1: len(userWeights[3])-2] +'", },'
        
        except Exception as e:
            serialized_items = {"getWeights": False, "Error Message":str(e)}
            return jsonify(serialized_items)
        
        finaloutput=finaloutput[0:len(finaloutput)]+"]"
        print(finaloutput)

# TODO - API call to update user weight.
# Stored Procedure Name: "spWeightUpdate"
@app.route('/api/updateuserweight', methods=['POST'])
def updateUserWeight():
        uwID = request.json['uwID']
        uwDate = request.json['uwDate']
        uwWeight = request.json['uwWeight']
        
     
        tempUserWeight = UserWeight(None, None, None)
        
    
        if updateUserWeight.update(uwID,uwDate,uwWeight) == True:
                 serialized_items = {"User Weight Updated": True}
        else:
                serialized_items = {"User Weight Updated": False}
              
                return jsonify(serialized_items)

# TODO - API call to delete user weight.
# Stored Procedure Name: "spWeightDelete"
@app.route('/api/deleteuserweight', methods=['POST'])
def deleteUserWeight():
         serialized_items = {"": ""}
         return jsonify(serialized_items)

# API call used for testing the connection between the frontend and the backend.
@app.route('/api/test', methods=['GET'])
def test_connection():
    serialized_items = {"message": "Hello", "connected_to_backend": True}
    return jsonify(serialized_items) # Send as a JSON so the frontend can consume it