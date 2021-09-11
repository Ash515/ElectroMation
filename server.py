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
def customerlogin():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)