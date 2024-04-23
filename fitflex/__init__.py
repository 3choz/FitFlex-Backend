import os
import json

from flask import (Flask, jsonify, render_template, request)
from flask_cors import CORS

from fitflex.Password import Password
from fitflex.User import User
from fitflex.Program import Program
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
    mylist=DBQuery("EXEC spGetPrograms")
    finaloutput="["
    for x in mylist:
        program = x.split(", ")
        finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
    finaloutput=finaloutput[0:len(finaloutput)-1]+"]"
    #print(json.dumps(finaloutput))
    serialized_items = {"message": "Hello", "output": mylist}
    return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it

# TODO - API Call for getting all Programs by difficulty for program selection
# Stored Procedure Name: "" - Need to make this - Shaun
@app.route('/api/getprogramsbydifficulty', methods=['GET'])
def getProgramsByDifficulty():
    mylist=DBQuery("EXEC spGetProgramsByDifficulty")
    finaloutput="["
    for x in mylist:
        program = x.split(", ")
        finaloutput = finaloutput + '{"prgmID": ' + program[0][1:] + ', "prgmName": "' + program[1][1: len(program[1])-1] + '", "prgmDescription": "' + program[2][1: len(program[2])-1]  + '", "prgmDifficulty": "' + program[3][1: len(program[3])-2] +'"},'
    finaloutput=finaloutput[0:len(finaloutput)-1]+"]"
    #print(json.dumps(finaloutput))
    serialized_items = {"message": "Hello", "output": mylist}
    return jsonify(json.loads(finaloutput)) # Send as a JSON so the frontend can consume it.

# TODO - API call for updating the user's program.
# Stored Procedure Name: "spSetUserProgram"
@app.route('/api/updateprogram', methods=['POST'])
def updateProgram():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call for getting the user's program.
# Stored Procedure Name: "getProgram"
@app.route('/api/getprogram', methods=['GET'])
def getProgram():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call for getting all exercises relating to user's program.
# Stored Procedure Name: "" - Need to make this - Shaun
@app.route('/api/getuserexercise', methods=['POST'])
def getUserExercises():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call for getting all records relating to a user's specific exercise.
# Stored Procedure Name: "spGetUserExercises"
@app.route('/api/getuserexercises', methods=['POST'])
def getUserExercise():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call for creating a user's exercise record.
# Stored Procedure Name: "spUserExerciseInsert"
@app.route('/api/createuserexercise', methods=['POST'])
def createUserExercise():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# Stored Procedure Name: "spUserExerciseUpdate"
# TODO - API call for updating a user's exercise record.
@app.route('/api/updateuserexercise', methods=['POST'])
def updateUserExercise():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# Stored Procedure Name: "spUserExerciseDelete"
# TODO - API call for deleting a user's exercise record.
@app.route('/api/deleteuserexercise', methods=['POST'])
def deleteUserExercise():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# Stored Procedure Name: "spGetUser"
# TODO - API call to get user data for profile page for viewing and updating
@app.route('/api/getuser', methods=['POST'])
def getUser():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call for the updating user. It will be used under the account page.
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

# TODO - API call to update password for the user.
# Stored Procedure Name: "spPasswordUpdate"
@app.route('/api/updatepassword', methods=['POST'])
def updatePassword():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call to view user weight.
# Stored Procedure Name: "spGetWeight"
@app.route('/api/getuserweight', methods=['POST'])
def getUserWeight():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call to view user weights.
# Stored Procedure Name: "spGetWeights"
@app.route('/api/getuserweights', methods=['POST'])
def getUserWeights():
    serialized_items = {"": ""}
    return jsonify(serialized_items)

# TODO - API call to update user weight.
# Stored Procedure Name: "spWeightUpdate"
@app.route('/api/updateuserweight', methods=['POST'])
def updateUserWeight():
    serialized_items = {"": ""}
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