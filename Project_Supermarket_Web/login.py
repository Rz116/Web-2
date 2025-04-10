from flask import Flask, request, render_template, redirect
import os.path
from os import path

fileDir = os.path.dirname(os.path.realpath("__file__"))
filename = "Ryan" + ".doc"
file = open(filename, "x")
file.write("Ryan" + "\n" + "Zhang")
file.close()

app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])
def main():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("login.html")
        check()
@app.route("/home",methods = ["GET","POST"])
def check():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    
    username  = request.form.get("username")
    password = request.form.get("password")
    
    filename = username + ".doc"
    filexist = bool(path.exists(filename))

    if(filexist == False):
        return render_template("login.html")
    else:
        admin = open(filename, "r")
        adminvalue = admin.read().splitlines()

        usercheck = adminvalue[0].strip()
        passcheck = adminvalue[1].strip()
        print(usercheck ,username, passcheck,password)
        if(username == usercheck and password == passcheck):
            print("correct")
            return render_template("home.html")
        else:
            print("wrong")
            return render_template("login.html")

@app.route("/signup",methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return render_template("signup.html")
        create()
def create():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    filename = username + ".doc"



    
if __name__ == "__main__":
    app.run()
