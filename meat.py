from flask import Flask, request, render_template, redirect,url_for
import os
import main
app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])
def Meat (nameuser):
    global price, items, amount, unit, username, adminvalue,admin2value
    username = nameuser
    admin = open("Meat.txt", "r")
    adminvalue = admin.read().split(",")
    admin2 = open("MeatPrices.txt", "r")
    admin2value = admin2.read().split(",")
    price = []
    items = []
    amount = []
    unit = []
    return render_template("meat.html", meat = adminvalue, price = admin2value)
@app.route("/meat_steak", methods = ["GET","POST"])
def meat_steak():
    if request.method == "GET":  
        return render_template("meat_steak.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_steak.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_steak.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[0])
            price.append(total_price)
            items.append("Steak")
            amount.append(quantity)
            unit.append("Lbs")

            file()
            return render_template("meat_steak.html" , product = adminvalue, price = admin2value)
        
@app.route("/meat_ground", methods = ["GET","POST"])
def meat_ground():
    if request.method == "GET":  
        return render_template("meat_ground.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_ground.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_ground.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[1])
            price.append(total_price)
            items.append("Ground Beef")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("meat_ground.html", product = adminvalue, price = admin2value)

@app.route("/meat_pork_ground", methods = ["GET", "POST"])
def meat_pork_ground():
    if request.method == "GET":  
        return render_template("meat_pork_ground.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_pork_ground.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_pork_ground.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[2])
            price.append(total_price)
            items.append("Ground Pork")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("meat_pork_ground.html", product = adminvalue, price = admin2value)
        
@app.route("/meat_pork_chop", methods = ["GET", "POST"])
def meat_pork_chop():
    if request.method == "GET":  
        return render_template("meat_pork_chop.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_pork_chop.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_pork_chop.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[3])
            price.append(total_price)
            items.append("Pork Chops")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("meat_pork_chop.html", product = adminvalue, price = admin2value)

@app.route("/meat_lamb_chop", methods = ["GET","POST"])
def meat_lamb_chop():
    if request.method == "GET":  
        return render_template("meat_lamb_chop.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_lamb_chop.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_lamb_chop.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[4])
            price.append(total_price)
            items.append("Lamb Chops")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("meat_lamb_chop.html", product = adminvalue, price = admin2value)

@app.route("/meat_bacon", methods = ["GET", "POST"])
def meat_bacon():
    if request.method == "GET":  
        return render_template("meat_bacon.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_bacon.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_bacon.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[5])
            price.append(total_price)
            items.append("Bacon ")
            amount.append(quantity)
            unit.append("Packs")

            file()
            return render_template("meat_bacon.html", product = adminvalue, price = admin2value)

@app.route("/meat_belly", methods = ["GET", "POST"])
def meat_belly():
    if request.method == "GET":  
        return render_template("meat_belly.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_belly.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_belly.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[6])
            price.append(total_price)
            items.append("Pork Belly")
            amount.append(quantity)
            unit.append("Lbs")

            file()
            return render_template("meat_belly.html", product = adminvalue, price = admin2value)

@app.route("/meat_mutton", methods = ["GET","POST"])
def meat_mutton():
    if request.method == "GET":  
        return render_template("meat_mutton.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("meat_mutton.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("meat_mutton.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[7])
            price.append(total_price)
            items.append("Ground Mutton")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("meat_mutton.html", product = adminvalue, price = admin2value)
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
