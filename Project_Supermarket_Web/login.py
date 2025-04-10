from flask import Flask, request, render_template, redirect,url_for
import os.path
from os import path

app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])

def main():
    print("main")
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("login.html")
        check()
@app.route("/",methods = ["GET","POST"])
def check():
    print("check")
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

@app.route("/signup",methods = ["GET"])
def signup():
    print("Signup")
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return render_template("home.html")
        home()
@app.route('/home',methods = ["GET","POST"])
def home():
    print("hello")
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    filename = str(username) + ".doc"
    fileexist = bool(path.exists(filename))
    print(username, password, email)
    if (username == "" or password == "" or email == ""):
        return render_template("signup.html")
    else:
        check = len(password)
        if (check < 6 ):
            return render_template ("signup.html")
        else:
            
            if (fileexist == False):
                admin = open(filename, "x")
                admin.write(username + "\n" + password + "\n" + email)
                admin.close()
                print("checkinput")
            else:
                return redirect(url_for('home'))
            
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()
