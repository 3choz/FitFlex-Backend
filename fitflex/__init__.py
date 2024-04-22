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

# Used for testing the connection between the frontend and the backend   
@app.route('/api/test', methods=['GET'])
def test_connection():
    serialized_items = {"message": "Hello", "connected_to_backend": True}
    return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

# Used for getting all Programs for program selection
@app.route('/api/getPrograms', methods=['GET'])
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

# API call for creating a user. This will be called under the create account page.
@app.route('/api/CreateUser', methods=['POST'])
def Create_User():
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

# API call for the Updating user. It will be used under the account page.
@app.route('/api/UpdateUser', methods=['POST'])
def Update_User():
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