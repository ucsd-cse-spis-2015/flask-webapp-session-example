import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# Just type some arbitrary letters and numbers.
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key='w98fw9ef8hwe98fhwef'; 

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["favoriteColor"]=request.form['favoriteColor']
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=54321)
