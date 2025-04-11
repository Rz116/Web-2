from flask import Flask, request, render_template, redirect,url_for
import os.path
from os import path

app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("home.html")
        check()
@app.route("/loginhome",methods = ["GET","POST"])
def check():
    global username, password
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    
    username  = request.form.get("username")
    password= request.form.get("password")
    if(username ==  "" or password == ""):
        return render_template("login.html")
    else:     
        filename = username + ".doc"
        filexist = bool(path.exists(filename))
    
        if(filexist == False):
            return render_template("login.html", check = "Username incorrect or doesnt exist")
        else:
            admin = open(filename, "r")
            adminvalue = admin.read().splitlines()
            
            usercheck = adminvalue[0].strip()
            passcheck = adminvalue[1].strip()
            print(username, password)
            if(username == usercheck and password == passcheck):
                print("correct")
                return render_template('home.html')
            else:
                print("wrong")
                return render_template("login.html", check = "Password incorrect")

@app.route("/signup",methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return render_template('signup.html')
        home2()
@app.route("/signuphome",methods = ["GET","POST"])
def home2():
    global username, password, email
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    
    userinfo = str(username) + ".doc"
    userproducts = str(username) + "products" + ".doc"
    userprice = str(username) + "prices" + ".doc"
    userquantity = str(username) + "quantity" + ".doc"
    reciept = str(username) + "reciept" + ".doc"
     
    fileexist = bool(path.exists(userinfo))
    fileexist2 = bool(path.exists(userproducts))
    fileexist3 = bool(path.exists(userprice))
    fileexist4 = bool(path.exists(userquantity))
    fileexist5 = bool(path.exists(reciept))
    
    if (username == "" or password == "" or email == ""):
        return render_template("signup.html")
    else:
        check = len(password)
        if (check < 6 ):
            return render_template ("signup.html")
        else:
            check = email.isdigit()
            if(check == True):
                return render_template("signup.html")
            else:
                if (fileexist == False):
                    adminuserinfo = open(userinfo, "x")
                    adminuserinfo.write(username + "\n" + password + " \n" + email + "\n" + str(0))
                    adminuserinfo.close()
                else:
                    return render_template("login.html", check = "Login already exists, Please sign in")
            
                if (fileexist2 == False):
                    adminproducts = open(userproducts, "x")
                    adminproducts.close()
                else:
                    return render_template("login.html", check = "Login already exists, Please sign in")
            
                if (fileexist3 == False):
                    adminprice = open(userprice, "x")
                    adminprice.close()
                else:
                    return render_template("login.html", check = "Login already exists, Please sign in")
            
                if (fileexist4 == False):
                    adminquantitiy = open(userquantity, "x")
                    adminquantitiy.close()
                else:
                    return render_template("login.html", check = "Login already exists, Please sign in")
                if (fileexist5 == False):
                    adminreciept = open(reciept, "x")
                    adminreciept.close()
                else:
                    return render_template("login.html", check = "Login already exists, Please sign in")

    return render_template("home.html")
@app.route('/home',methods = ["GET","POST"])
def home():
    return render_template("home.html")

@app.route('/profile', methods = ["GET","POST"])
def profile():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filename = username  + ".doc"
    exists = bool(path.exists(filename))
    if (exists == False):
        return render_template("home.html")
    else:
        adminfile = open(filename, "r")
        adminvalue = adminfile.read().splitlines()
        user = adminvalue[0].strip()
        passed = adminvalue[1].strip()
        mail = adminvalue[2].strip()
        orders = adminvalue[3].strip()
        
    return render_template("profile.html", username = user, passed = passed, email = mail, count = orders)

if __name__ == "__main__":
    app.run()
