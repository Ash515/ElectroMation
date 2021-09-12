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
            return redirect(url_for('custmain'))
        else:
            # Account doesnt exist or username/password incorrect
             message = 'Incorrect username/password!'
    return render_template('/customer interface/customerlogin.html', message='')

@app.route('/adminlogin',methods=['POST','GET'])
def adminlogin():
    message="Please fill the login "
    if request.method=='POST':
        adminname=request.form['adminid']
        adminpassword=request.form['adminpass']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admincredentials WHERE username = %s AND password = %s', (adminname,adminpassword))
        admin=cursor.fetchone()
        if admin:
            session['loggedin'] = True
            session['adminid'] = admin['username']
            session['adminpass'] = admin['password']
            return redirect(url_for('adminmain'))
        else:
            # Account doesnt exist or username/password incorrect
             message = 'Incorrect username/password!'
    return render_template('/admin interface/adminlogin.html', message='')

@app.route('/customermain')
def custmain():
    if 'loggedin' in session:
        eb_id=session['EBID']
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM customerregistration where ebid=%s',(eb_id,))
        detail=cur.fetchall()
    return render_template('/customer interface/customermain.html',Ebid=detail)

@app.route('/adminmain')
def adminmain():
    if 'loggedin' in session:
        admin_id=session['adminid']
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM admincredentials where username=%s',(admin_id,))
        admindetail=cur.fetchall()
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM customerregistration')
        customerlist=cur.fetchall()
    return render_template('/admin interface/adminmain.html',Admin_id=admindetail,customer_list=customerlist)

@app.route('/customerlogout')
def customerlogout():
   session.pop('EBID')
   return redirect(url_for('index'))

@app.route('/adminlogout')
def adminlogout():
   session.pop('adminid')
   return redirect(url_for('index'))

@app.route('/readingpage/<ebid>',methods=['POST','GET'])
def readingpage(ebid):
     
     cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
     cur.execute('SELECT * FROM estimation where ebid=%s',(ebid,))
     readingdetails=cur.fetchall()
     return render_template('/admin interface/adminentry.html',readings=readingdetails)

@app.route('/proceed',methods=["POST","GET"])
def proceed():
    if request.method=='POST':
        ebid=request.form['EBID']
        amt=request.form['payment']
        msg=request.form['payment-msg']
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('INSERT INTO paymentdetails VALUES(%s,%s,%s)',(ebid,amt,msg))
       
        return redirect(url_for('notify'))
    return render_template('/admin interface/proceed.html')

@app.route('/notify',methods=['POST','GET'])
def notify():
    return render_template('notify.html')
if __name__=="__main__":
    app.run(debug=True)