from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new-module', methods=['GET','POST'])
def new_module():
  if request.method == 'GET':
    return show_module_composer()
  elif request.method == 'POST':
    return create_new_module(request.data)

@app.route('/module/<id>', methods=['GET'])
def view_module(id):
  if request.method == 'GET':
    return show_module_viewer(id)

def show_module_composer():
  return render_template('new-module.html', name='Ben')

def create_new_module():
  return 'create new module'

def show_module_viewer(id):
  return 'id ' + id 

if (__name__ == '__main__'):
	app.run(debug=True, threaded=True)