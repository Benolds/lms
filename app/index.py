from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# import models.module
import models.user
from models.module import create_module

db.create_all() 

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new-module', methods=['GET','POST'])
def new_module():
  if request.method == 'GET':
    return show_module_composer()
  elif request.method == 'POST':
    return create_new_module(request.form)

@app.route('/module/<id>', methods=['GET'])
def view_module(id):
  if request.method == 'GET':
    return show_module_viewer(id)

def show_module_composer():
  return render_template('new-module.html')

def create_new_module(form_data):
  create_module(form_data['title'], form_data['body'])
  return 'create new module'

def show_module_viewer(id):
  return 'viewing module with id ' + id 

if (__name__ == '__main__'):
	app.run(debug=True, threaded=True)