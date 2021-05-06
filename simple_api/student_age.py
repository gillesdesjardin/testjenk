#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth
from flask import g, session, redirect, url_for
from flask_simpleldap import LDAP
import json
import os

auth = HTTPBasicAuth()
app = Flask(__name__)
app.debug = True

@auth.get_password
def get_password(username):
    if username == 'toto':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


try:
    student_age_file_path
    student_age_file_path  = os.environ['student_age_file_path'] 
except NameError:
    student_age_file_path  = '/home/desjardin/student_age.json'

student_age_file = open(student_age_file_path, "r")
student_age = json.load(student_age_file)
print(student_age)
student_age_file.close()

@app.route('/get_student_ages', methods=['GET'])
@auth.login_required
def get_student_ages():
    print("get_student_ages")
    return jsonify({'student_ages': student_age })

#student_name =request.args.get('student_name', default = '*', type = str)
#@app.route('/get_student_ages/<student_name>', methods=['GET'])

@app.route('/user/<string:name>/', methods=['GET', 'POST'])
def user_view(name):
    print(name)
    return(name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    print(username)
    password = request.args.get('password')
    print(password)
    return(username)

@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    print(year)
    print(month)
    print(title)
    return title
            
@app.route('/get_student_age/<student_name>', methods=['GET'])
def get_student_age(student_name):
    print(student_name)
    student_age_file_path  = '/home/desjardin/student_age.json'
    student_age_file = open(student_age_file_path, "r")
    student_age = json.load(student_age_file)
    print(student_age)
    student_age_file.close()
    print("get_student_age:")
    print(student_age)
    if student_name not in student_age :
        print("error not found in")
        print(student_age)
        abort(404)
    if student_name in student_age :
      age = student_age[student_name]
      print(age)
      del student_age[student_name]
      with open(student_age_file_path, 'w') as student_age_file:
        json.dump(student_age, student_age_file, indent=4, ensure_ascii=False)
    return age 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
