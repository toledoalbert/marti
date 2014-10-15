#import the flask class. an instance of this class will be our bricksquad application
#from final6 import app
import tweeql
#return 1
import threading
import re
import subprocess
from subprocess import call
#from tweeql import *
import flask, flask.views, os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app,  _app_ctx_stack
import sqlalchemy
from sqlalchemy import MetaData, create_engine, Table, select
#import flask.ext.script
#from flask.ext.script import Manager, Command, Option
from sqlalchemy.ext.declarative import declarative_base
#from tweeql.field_descriptor import ReturnType
#from tweeql.function_registry import FunctionInformation, FunctionRegistry
#from tweeql.query_runner import QueryRunner
#from tweeql.exceptions import TweeQLException
#Sfrom multiprocessing import Process
from werkzeug.utils import secure_filename
#return 'sleep'
#import settings


POOL_TIME = 15 #Seconds

# variables that are accessible from anywhere
#commonDataStruct = {}
# lock to control access to variable
#dataLock = threading.Lock()
# thread handler
#yourThread = threading.Thread()

app = flask.Flask(__name__)
app.secret_key = "bricksquad"
#Specify where you want your uploaded files to go
UPLOAD_FOLDER = '/home/'
ALLOWED_EXTENSIONS = set(['txt'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#Enter database information
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'

#REGEX =''
#manager = Manager(app)
res = ''
global regexpression
regexpression = []

global filename

#Method to query tweets from the database
def getData():
    # Enter database URI
    engine = create_engine('mysql://', echo=True)
    mymetadata = MetaData(engine)
    easter = 'easter'
    Base = declarative_base(metadata=mymetadata)
    users = Table('easter', mymetadata, autoload=True)
    s = select([users])
    result = engine.execute(s)
    alltweets = []
    count = 0
    for row in result:
        #alltweets[count] = row
        alltweets.append(row)
        #count=count+1
    return alltweets

#File Upload methods
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    filename =''
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            Upload.filename = filename
            return redirect(url_for('uploaded_file',filename=filename))
        else:
            return redirect(url_for('upload_error',filename=filename))
class Upload(flask.views.MethodView):
    @app.route('/uploaded_file', methods=['GET', 'POST'])
    def uploaded_file():
        return flask.render_template('upload.html')
    @app.route('/upload_error', methods=['GET', 'POST'])
    def upload_error():
        return flask.render_template('invalidfile.html')

'''
@manager.command
def runSearch(cmd):
    runner = QueryRunner()
    stmt = "select text from twitter into table " + cmd + " where text contains "+ "'" + cmd +"'"
    runner.run_query(stmt, False)
    manager.add_command('runit', runSearch('resultine'))
    threading.Thread(target=manager.add_command('runit', runSearch('you'))).start()
    threading.Thread(target=run_script(0, 'aprilyermen')).start()
    run_script(0, 'aprilyermen')
    getData()
'''
#@manager.command
def runSearch(cmd):
    runner = QueryRunner()
    stmt = "select text from twitter into table " + cmd + " where text contains "+ "'" + cmd +"'"
    runner.run_query(stmt, False)

global result
#Main View
class View(flask.views.MethodView):
    result = ''
    def get(self):
    	#user = {} # fake user
    	return flask.render_template('newhome.html')

    @app.route('/', methods=['POST'])
    def post(self):
        result = flask.request.form['expression']
        res = result
        #app.start()
       #global commonDataStruct
       #commonDataStruct = {result}
       #dbHandler()
        #session['username'] = result
        #Most WHERE clauses can be constructed via normal comparisons
        #s = users.select(users.c.name == 'easter')
        #run(s)
        #getData(self)
        #Result.get(result)
       #entries = getData()
       #manager.run()
        #threading.Thread(target=manager.add_command('runit', runSearch(result))).start()
        #try:
            #threading.Thread(target=manager.add_command('runit', runSearch(result))).start()
            #p = Process(target =manager.add_command('runit', runSearch('resultine')))
            #p.start()
        #except:
         #   return 'Fucking fail'
         #flask.render_template('result.html', expression=result, tweets = entries)

class Result(flask.views.MethodView):
    @app.route('/result',methods=['GET','POST'])
    def get():
        result = res
        entries = getData()
        return flask.render_template('result.html', expression = result, tweets = entries)

    @app.route('/weathermap')
    def weather():
        return flask.render_template('weathermap.html')

    @app.route('/aboutme')
    def about():
        return flask.render_template('aboutme.html')

#Create methods to run search in the background

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])
app.add_url_rule('/result', view_func=View.as_view('result'), methods=['GET', 'POST'])
app.add_url_rule('/aboutme', view_func=View.as_view('aboutme'), methods=['GET', 'POST'])
app.debug = True;


if __name__ == '__main__':
    app.run()