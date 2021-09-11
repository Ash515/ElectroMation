from flask import Flask,send_file, render_template,send_file,url_for,redirect,flash, request, redirect,session
import os,datetime
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app=Flask(__name__,template_folder='template')
app.secret_key="key"
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="electromation"
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customerlogin',methods=['POST','GET'])
def customerlogin():
    message="Please fill the login "
    if request.method=='POST':
        ebid=request.form['EBID']
        passcode=request.form['passcode']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM customerregistration WHERE ebid = %s AND password = %s', (ebid, passcode))
        customer=cursor.fetchone()
        if customer:
            session['loggedin'] = True
            session['EBID'] = customer['ebid']
            session['passcode'] = customer['password']
            return redirect(url_for('main'))
        else:
            # Account doesnt exist or username/password incorrect
             message = 'Incorrect username/password!'
    return render_template('/customer interface/customerlogin.html', message='')


if __name__=="__main__":
    app.run(debug=True)