import os

from flask import (Flask, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_cors import CORS

from fitflex.Password import Password

app = Flask(__name__, template_folder= os.path.abspath("./templates"), static_folder=os.path.abspath("./static"))
CORS(app) #Enable CORS for all routes
#os.chdir("..")
#template_dir = os.path.abspath()
print("directory: " + os.getcwd())
print(os.path.abspath("./templates"))
@app.route('/')

def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   formEmail = request.form.get('email')
   formPassword = request.form.get('password')
   if formEmail:
       attempt = Password()
       if attempt.login(formEmail,formPassword) == True:
           status = "True"
       else:
           status = "False"
       return render_template('hello.html', status = status)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

# Use for testing the connection between the frontend and the backend   
@app.route('/api/test', methods=['GET'])
def test_connection():
    serialized_items = {"message": "Hello", "connected_to_backend": True}
    return jsonify(serialized_items) # Send as a JSON so the frontend can consume it

