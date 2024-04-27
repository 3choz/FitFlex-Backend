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
from fitflex.DBConnect import DBQuery


app = Flask(__name__, template_folder = os.path.abspath("./templates"), static_folder=os.path.abspath("./static"))
CORS(app) # Enable CORS for all routes

@app.route('/')

def index():
   print('Request for index page received')
   return render_template('index.html')

# Validated - API call for the logging in the user. 
@app.route('/api/login', methods=['POST'])
def login():
    try:
        userEmail = request.json['userEmail']    
        userPassword = request.json['userPassword']
        tempPass = Password()
        serialized_items=""
    
        if tempPass.login(userEmail,userPassword) == True:
            serialized_items = {"Database Operation": True}
        else:
            serialized_items = {"Database Operation": False}

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
    return jsonify(serialized_items)

# Validated - API call for creating a user. This will be called under the create account page.
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
            serialized_items = {"Database Operation": True}
        else:
            serialized_items = {"Database Operation": False}

    except Exception as e:
        serialized_items = {"Database Operation": False, "Error Message":str(e)}

    return jsonify(serialized_items) 

# Validated - Used for getting all Programs for program selection
@app.route('/api/getprograms', methods=['GET'])
def getPrograms():
    try:
        mylist = DBQuery("EXEC spGetPrograms")
        finaloutput="["
        for x in mylist:
            program = x.split(", ")
            finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
        finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

        return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) 

# Validated - API Call for getting all Programs by difficulty for program selection
@app.route('/api/getprogramsbydifficulty', methods=['POST'])
def getProgramsByDifficulty():
    try:
        prgmDifficulty = request.json['prgmDifficulty']

        mylist = DBQuery("EXEC spGetProgramByDifficulty @Difficulty='" + prgmDifficulty + "'")
        finaloutput="["
        if len(mylist) > 0:
            for x in mylist:
                program = x.split(", ")
                try:
                    finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
                except Exception as e:
                    serialized_items = {"Database Operation": False,"Error Message":str(e)}
                    return jsonify(serialized_items)
            finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

            return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

    except Exception as e:
        serialized_items = {"Database Operation": False, "Error Message":str(e)}
        return jsonify(serialized_items) 

# Validated - API call for updating the user's program.
@app.route('/api/updateprogram', methods=['POST'])
def updateProgram():
    try:
        userEmail = request.json['userEmail']
        prgmID = request.json['prgmID']

        tempUser = User(userEmail,None, None, None, None, None, None, None)

        if tempUser.updateProgram(prgmID):
            serialized_items = {"Database Operation": True}
        else:
            serialized_items = {"Database Operation": False}
        return jsonify(serialized_items)

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) 

# Validated - API call for getting the user's program.
@app.route('/api/getprogram', methods=['GET'])
def getProgram():
    try:
        userEmail = request.json['userEmail'] 

        mylist = DBQuery("EXEC spGetProgram @Email='" + userEmail + "'")
        finaloutput="["
        if len(mylist) > 0:
            for x in mylist:
                program = x.split(", ")
                try:
                    finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
                except Exception as e:
                    serialized_items = {"Database Operation": False,"Error Message":str(e)}
                    return jsonify(serialized_items)
            finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

        return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) 

# Validated - API call for getting all exercises relating to user's program.
@app.route('/api/getusersexercises', methods=['POST'])
def getUserExercise():
    try:
        userEmail = request.json['userEmail'] 
        mylist = DBQuery("EXEC spGetExerciseByUserProgram @Email='" + userEmail + "'")

        finaloutput="["
        if len(mylist) > 0:
            for x in mylist:
                program = x.split(", ")

                try:
                    finaloutput = finaloutput + '{"exID": ' + program[0][1:] + ','
                    finaloutput = finaloutput + '"prgmID": ' + program[1] + ','
                    finaloutput = finaloutput + '"exName": "' + program[3][1: len(program[3])-1] + '",'
                    finaloutput = finaloutput + '"exDescription": "' + program[4][1: len(program[4])-1] + '",'
                    finaloutput = finaloutput + '"exVideolink": "' + program[5][1: len(program[5])-1] + '",'
                    finaloutput = finaloutput + '"exTrainerSex": "' + program[6][1: len(program[6])-1] + '",'
                    finaloutput = finaloutput + '"exVideolength": ' + program[7][0: len(program[7])-1] + '},'
                
                except Exception as e:
                    serialized_items = {"Database Operation": False,"Error Message":str(e)}
                    return jsonify(serialized_items)

            finaloutput=finaloutput[0:len(finaloutput)-1]+"]"
            print(finaloutput)
            return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) 

# Validated - API call for getting all exercises relating to user's program.
@app.route('/api/getuserexercisesbyexercise', methods=['POST'])
def getUserExercisesByExercise():
    try:
        userEmail = request.json['userEmail']
        exID = request.json['exID'] 
        mylist = DBQuery("EXEC spGetUserExercises @Email='" + userEmail + "', @ID=" + str(exID))

        finaloutput="["
        if len(mylist) > 0:
            for x in mylist:
                program = x.split(", ")

                try:
                    finaloutput = finaloutput + '{"ueID": ' + program[0][1:] + ', "exID": ' + program[1]+', "userEmail": "' + program[2][1: len(program[2])-1] + '", "ueDate": "' + program[3][14: ] +"/"+program[4]+ "/" + program[5][0:len(program[5])-1] + '", "ueType": "' + program[6][1: len(program[6])-1] + '", "ueAmount": ' + program[7][9: len(program[7])-3] +'},'
                except Exception as e:
                    serialized_items = {"Database Operation": False,"Error Message":str(e)}
                    return jsonify(serialized_items)
            finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

            return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.
    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) 

# Validated - API call for get record relating to a user's specific exercise.
@app.route('/api/getuserexercise', methods=['POST'])
def getUserExercises():
    try:
        ueID = request.json['ueID'] 
        mylist = DBQuery("EXEC spgetuserexercise @ID=" + str(ueID))
        finaloutput="["
        if len(mylist) > 0:
            for x in mylist:
                program = x.split(", ")
                try:
                    finaloutput = finaloutput + '{"ueID": ' + program[0][1:] + ', "exID": ' + program[1]+', "userEmail": "' + program[2][1: len(program[2])-1] + '", "ueDate": "' + program[3][14: ] +"/"+program[4]+ "/" + program[5][0:len(program[5])-1] + '", "ueType": "' + program[6][1: len(program[6])-1] + '", "ueAmount": ' + program[7][9: len(program[7])-3] +'},'
                except Exception as e:
                    serialized_items = {"Database Operation": False,"Error Message":str(e)}
                    return jsonify(serialized_items)
            finaloutput=finaloutput[0:len(finaloutput)-1]+"]"

            return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) 

# Validated - API call for creating a user's exercise record.
@app.route('/api/createuserexercise', methods=['POST'])
def createUserExercise():
    try:
        exID = request.json['exID']
        userEmail = request.json['userEmail']
        ueDate = request.json['ueDate']
        ueType = request.json['ueType']
        ueAmount = request.json['ueAmount']

        newUserExercise = UserExercise(None,exID, userEmail,ueDate,ueType,ueAmount)

        if newUserExercise.create() == True:
            serialized_items = {"Database Operation": True}
        else:
            serialized_items = {"Database Operation": False}

    except Exception as e:
        serialized_items = {"Database Operation": False, "Error Message":str(e)}

    return jsonify(serialized_items)

# Validated - API call for updating a user's exercise record.
@app.route('/api/updateuserexercise', methods=['POST'])
def updateUserExercise():
    try:
        ueID = request.json['ueID']
        ueDate = request.json['ueDate']
        ueType = request.json['ueType']
        ueAmount = request.json['ueAmount']
        
        tempUserExcercise = UserExercise(ueID, None, None, None, None, None)

        if tempUserExcercise.update(ueDate,ueType,ueAmount):
             serialized_items = {"Database Operation": True}
        else:
             serialized_items = {"Database Operation": False}
        return jsonify(serialized_items)

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

# Validated - API call for deleting a user's exercise record.
@app.route('/api/deleteuserexercise', methods=['POST'])
def deleteUserExercise():
    try:
        ueID = request.json['ueID']

        tempUserExcercise = UserExercise(ueID, None, None, None, None, None)

        if tempUserExcercise.delete() == True:
             serialized_items = {"Database Operation": True}
        else:
             serialized_items = {"Database Operation": False}
        return jsonify(serialized_items)

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

# Validated - API call to get user data for profile page for viewing and updating
@app.route('/api/getuser', methods=['POST'])
def getUser():
    try:
        userEmail = request.json['userEmail']
        mylist = DBQuery("EXEC spGetUser @Email='" + userEmail + "'")
        finaloutput="{"
        if len(mylist) > 0:
            for x in mylist:
                program = x.split(", ")
                try:
                    if len(program) == 9:
                        # The user has no program assigned
                        finaloutput = finaloutput + f'"userEmail": "{program[0][2:len(program[0])-1]}",'
                        finaloutput = finaloutput + f'"passID": {program[1]},'
                        finaloutput = finaloutput + f'"prgmID": 0,'
                        finaloutput = finaloutput + f'"userFirstName": "{program[2][1:len(program[2])-1]}",'
                        finaloutput = finaloutput + f'"userLastName": "{program[3][1:len(program[3])-1]}",'
                        finaloutput = finaloutput + f'"UserDOB": "{program[4][14:]}/{program[5]}/{program[6][0:len(program[6])-1]}",'
                        finaloutput = finaloutput + f'"userPhone": "{program[7][1:len(program[7])-1]}",'
                        finaloutput = finaloutput + f'"userSex": "{program[8][1:len(program[8])-2]}"'
                    else:
                        # The user has a program assigned 
                        finaloutput = finaloutput + f'"userEmail": "{program[0][2:len(program[0])-1]}",'
                        finaloutput = finaloutput + f'"passID": {program[1]},'
                        finaloutput = finaloutput + f'"prgmID": {program[2]},'
                        finaloutput = finaloutput + f'"userFirstName": "{program[3][1:len(program[3])-1]}",'
                        finaloutput = finaloutput + f'"userLastName": "{program[4][1:len(program[4])-1]}",'
                        finaloutput = finaloutput + f'"UserDOB": "{program[5][14:]}/{program[6]}/{program[7][0:len(program[7])-1]}",'
                        finaloutput = finaloutput + f'"userPhone": "{program[8][1:len(program[8])-1]}",'
                        finaloutput = finaloutput + f'"userSex": "{program[9][1:len(program[9])-2]}"'
                
                except Exception as e:
                    serialized_items = {"Database Operation": False,"Error Message":str(e)}
                    return jsonify(serialized_items)

            finaloutput = finaloutput + "}"

        return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

# Validated - API call for the updating user. It will be used under the account page.
@app.route('/api/updateuser', methods=['POST'])
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
            serialized_items = {"Database Operation": True}
        else:
            serialized_items = {"Database Operation": False,"Error Message":str(e)}
    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
    return jsonify(serialized_items)

# Validated - API call to update password for the user.
# Stored Procedure Name: "spPasswordUpdate"
@app.route('/api/updatepassword', methods=['POST'])
def updatePassword():
    try:
        userEmail = request.json['userEmail']    
        userPassword = request.json['userPassword']
        userNewPassword = request.json['userNewPassword']

        tempPass = Password()

        if(tempPass.login(userEmail,userPassword) == True):
            if (tempPass.update(userEmail, userPassword, userNewPassword) == True):
                return jsonify({"Database Operation": True})
            else:
                return jsonify({"Database Operation": False})
    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items)

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
            serialized_items = {"Database Operation": False,"Error Message":str(e)}
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
            serialized_items = {"Database Operation": False,"Error Message":str(e)}
            return jsonify(serialized_items)
        
        finaloutput=finaloutput[0:len(finaloutput)]+"]"
        print(finaloutput)

# TODO - API call to update user weight.
# Stored Procedure Name: "spWeightUpdate"
@app.route('/api/updateuserweight', methods=['POST'])
def updateUserWeight():
    try:
        uwID = request.json['uwID']
        uwDate = request.json['uwDate']
        uwWeight = request.json['uwWeight']
        
        tempUserWeight = UserWeight(None, None, None, None)
        
        if tempUserWeight.update(uwID,None, uwDate,uwWeight) == True:
            serialized_items = {"Database Operation": True}
        else:
            serialized_items = {"Database Operation": False}
              
        return jsonify(serialized_items)

    except Exception as e:
        serialized_items = {"Database Operation": False, "Error Message":str(e)}
        return jsonify(serialized_items)


# TODO - API call to delete user weight.
# Stored Procedure Name: "spWeightDelete"
@app.route('/api/deleteuserweight', methods=['POST'])
def deleteUserWeight():
    try:
        uwID = request.json['uwID']
        tempUserWeight = UserWeight(uwID, None, None, None)
        if tempUserWeight.delete() == True:
            serialized_items = {"Database Operation": True}
        else:
            serialized_items = {"Database Operation": False}
        return jsonify(serialized_items)

    except Exception as e:
        serialized_items = {"Database Operation": False,"Error Message":str(e)}
        return jsonify(serialized_items)
