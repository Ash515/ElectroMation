from flask import Flask,send_file, render_template,send_file,url_for,redirect,flash, request, redirect,session
import os,datetime

app=Flask(__name__,template_folder='template')

@app.route('/')
def customerlogin():
    return render_template('/admin interface/admininbox.html')

if __name__=="__main__":
    app.run(debug=True)