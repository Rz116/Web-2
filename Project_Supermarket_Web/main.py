from flask import Flask, request, render_template, redirect,url_for
import os.path
from os import path

app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])

def main():
    global price, items, amount, unit
    price = []
    items = []
    amount = []
    unit = []
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

#poultry section
@app.route("/Poultry", methods = ["GET","POST"])
def Poultry():
    return render_template("poultry.html")

@app.route("/poultry_nuggets", methods = ["GET","POST"])
def poultry_nuggets():
    if request.method == "GET":  
        return render_template("poultry_nuggets.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_nuggets.html")
        else:
            total_price = int(quantity) * 4
            price.append(total_price)
            items.append("Frozen Nuggets")
            amount.append(quantity)
            unit.append("Packs")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_nuggets.html")
        
@app.route("/poultry_breast", methods = ["GET","POST"])
def poultry_breast():
    if request.method == "GET":  
        return render_template("poultry_breast.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_breast.html")
        else:
            total_price = int(quantity) * 5
            price.append(total_price)
            items.append("Chicken Breast")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_breast.html")

@app.route("/poultry_thighs", methods = ["GET", "POST"])
def poultry_thighs():
    if request.method == "GET":  
        return render_template("poultry_thighs.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_thighs.html")
        else:
            total_price = int(quantity) * 4.5
            price.append(total_price)
            items.append("Chicken Thighs")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_thighs.html")
        
@app.route("/poultry_whole", methods = ["GET", "POST"])
def poultry_whole():
    if request.method == "GET":  
        return render_template("poultry_whole.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_whole.html")
        else:
            total_price = int(quantity) * 6
            price.append(total_price)
            items.append("Whole chicken")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_whole.html")

@app.route("/poultry_wings")
def poultry_wings():
    if request.method == "GET":  
        return render_template("poultry_wings.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_wings.html")
        else:
            total_price = int(quantity) * 3.5
            price.append(total_price)
            items.append("Chicken wings")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_breast.html")

@app.route("/poultry_duck", methods = ["GET", "POST"])
def poultry_duck():
    if request.method == "GET":  
        return render_template("poultry_duck.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_duck.html")
        else:
            total_price = int(quantity) * 6.5
            price.append(total_price)
            items.append("Duck Breast")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_duck.html")

@app.route("/poultry_tenders", methods = ["GET", "POST"])
def poultry_tenders():
    if request.method == "GET":  
        return render_template("poultry_tenders.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_tenders.html")
        else:
            total_price = int(quantity) * 6.5
            price.append(total_price)
            items.append("Frozen Chicken Tenders")
            amount.append(quantity)
            unit.append("Packs")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_tenders.html")

@app.route("/poultry_drums", methods = ["GET","POST"])
def poultry_drums():
    if request.method == "GET":  
        return render_template("poultry_drums.html")
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_drums.html")
        else:
            total_price = int(quantity) * 3.5
            price.append(total_price)
            items.append("Chicken Drumsticks")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_drums.html")

#Meat department
@app.route("/Meat", methods = ["GET","POST"])
def Meat():
    return render_template("meat.html")

#Produce department
@app.route("/Produce", methods = ["GET","POST"])
def Produce():
    return render_template("produce.html")

#Beverages department
@app.route("/Beverages", methods = ["GET","POST"])
def Beverages():
    return render_template("drink.html")

#cart
@app.route("/cart",methods = ["GET","POST"])
def cart():
    global price, items, amount, unit
    total = 0
    if request.method == "GET":
        fileproduct = username + "products" + ".doc"
        adminfile2 = open(fileproduct, "r")
        adminfile2value = adminfile2.read().splitlines()
        adminfile2.close()
        
        fileprice = username + "prices" + ".doc"
        adminprice2 = open(fileprice, "r")
        adminprice2value = adminprice2.read().splitlines()
        adminprice2.close()
        
        filequantity = username + "quantity" + ".doc"
        adminquantity2 = open(filequantity, "r")
        adminquantity2value = adminquantity2.read().splitlines()
        adminquantity2.close()
        print(adminprice2value)
        for i in range(len(adminprice2value)):
            total = total + float(adminprice2value[i])
        length = len(adminprice2value)
        return render_template("cart.html", total = total, length = length, product = adminfile2value, Price = adminprice2value, Quantity = adminquantity2value)
    else:
        price = []
        items = []
        amount = []
        unit = []
        
        file1 = username + "products" + ".doc"
        adminfile = open(file1, "r+")
        adminfile.truncate()
        adminfile.close()

        file2 = username + "prices" + ".doc"
        adminfile2 = open(file2, "r+")
        adminfile2.truncate()
        adminfile.close()

        file3 = username + "quantity" + ".doc"
        adminfile3 = open(file3, "r+")
        adminfile3.truncate()
        adminfile.close()
        
        return profile()
def file():
    fileproduct = username + "products" + ".doc"
    adminfile = open(fileproduct, "w")
    for i in range(len(items)):
        adminfile.write(items[i] + "\n")
    adminfile.close()
    fileprice = username + "prices" + ".doc"
    adminprice = open(fileprice, "w")
    for i in range(len(price)):
        adminprice.write(str(price[i]) + "\n")
    adminprice.close()
    filequantity = username + "quantity" + ".doc"
    adminquantity = open(filequantity, "w")
    for i in range(len(amount)):
        adminquantity.write(str(amount[i]) + " " + unit[i] + "\n")
    adminquantity.close()
    
if __name__ == "__main__":
    app.run()
