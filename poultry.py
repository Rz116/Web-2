from flask import Flask, request, render_template, redirect,url_for
import os
import main
app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])
def Poultry (nameuser):
    global price, items, amount, unit, username, adminvalue,admin2value
    username = nameuser
    admin = open("Poultry.txt", "r")
    adminvalue = admin.read().split(",")
    admin2 = open("PoultryPrices.txt", "r")
    admin2value = admin2.read().split(",")
    price = []
    items = []
    amount = []
    unit = []
    return render_template("poultry.html", poultry = adminvalue, price = admin2value)
@app.route("/poultry_nuggets", methods = ["GET","POST"])
def poultry_nuggets():
    if request.method == "GET":  
        return render_template("poultry_nuggets.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_nuggets.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_nuggets.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[0])
            price.append(total_price)
            items.append("Frozen Nuggets")
            amount.append(quantity)
            unit.append("Packs")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_nuggets.html" , product = adminvalue, price = admin2value)
        
@app.route("/poultry_breast", methods = ["GET","POST"])
def poultry_breast():
    if request.method == "GET":  
        return render_template("poultry_breast.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_breast.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_breast.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[1])
            price.append(total_price)
            items.append("Chicken Breast")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_breast.html", product = adminvalue, price = admin2value)

@app.route("/poultry_thighs", methods = ["GET", "POST"])
def poultry_thighs():
    if request.method == "GET":  
        return render_template("poultry_thighs.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_thighs.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_thighs.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[2])
            price.append(total_price)
            items.append("Chicken Thighs")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_thighs.html", product = adminvalue, price = admin2value)
        
@app.route("/poultry_whole", methods = ["GET", "POST"])
def poultry_whole():
    if request.method == "GET":  
        return render_template("poultry_whole.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_whole.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_whole.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[3])
            price.append(total_price)
            items.append("Whole chicken")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_whole.html", product = adminvalue, price = admin2value)

@app.route("/poultry_wings", methods = ["GET","POST"])
def poultry_wings():
    if request.method == "GET":  
        return render_template("poultry_wings.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_wings.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_wings.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[4])
            price.append(total_price)
            items.append("Chicken wings")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_wings.html", product = adminvalue, price = admin2value)

@app.route("/poultry_duck", methods = ["GET", "POST"])
def poultry_duck():
    if request.method == "GET":  
        return render_template("poultry_duck.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_duck.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_duck.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[5])
            price.append(total_price)
            items.append("Duck Breast")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_duck.html", product = adminvalue, price = admin2value)

@app.route("/poultry_tenders", methods = ["GET", "POST"])
def poultry_tenders():
    if request.method == "GET":  
        return render_template("poultry_tenders.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_tenders.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_tenders.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[6])
            price.append(total_price)
            items.append("Frozen Chicken Tenders")
            amount.append(quantity)
            unit.append("Packs")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_tenders.html", product = adminvalue, price = admin2value)

@app.route("/poultry_drums", methods = ["GET","POST"])
def poultry_drums():
    if request.method == "GET":  
        return render_template("poultry_drums.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("poultry_drums.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("poultry_drums.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[7])
            price.append(total_price)
            items.append("Chicken Drumsticks")
            amount.append(quantity)
            unit.append("Pounds")

            print(price,items,amount,unit)
            file()
            return render_template("poultry_drums.html", product = adminvalue, price = admin2value)
def file():
    fileproduct = username + "products" + ".doc"
    adminfile =  open(fileproduct, "a")
    for i in range(len(items)):
        adminfile.write(items[i] + "\n")
    adminfile.close()
        
    fileprice = username + "prices" + ".doc"
    adminprice = open(fileprice, "a")
    for i in range(len(price)):
        adminprice.write(str(price[i]) + "\n")
    adminprice.close()
        
    filequantity = username + "quantity" + ".doc"
    adminquantity = open(filequantity, "a")
    for i in range(len(amount)):
        adminquantity.write(str(amount[i]) + " " + unit[i] + "\n")
    adminquantity.close()
if __name__ == "__main__":
    app.run()
