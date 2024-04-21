import os

from flask import (Flask, jsonify, render_template, request)

from fitflex.Password import Password
from fitflex.User import User

app = Flask(__name__, template_folder = os.path.abspath("./templates"), static_folder=os.path.abspath("./static"))

@app.route('/')

def index():
   print('Request for index page received')
   return render_template('index.html')

# Use for testing the connection between the frontend and the backend   
@app.route('/api/test', methods=['GET'])
def test_connection():
    serialized_items = {"message": "Hello", "connected_to_backend": True}
    return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

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