from flask import Flask, request, render_template, redirect,url_for
import os
import main
app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])
def Beverages(nameuser):
    global price, items, amount, unit, username, adminvalue,admin2value
    username = nameuser
    admin = open("Beverages.txt", "r")
    adminvalue = admin.read().split(",")
    admin2 = open("BeveragesPrices.txt", "r")
    admin2value = admin2.read().split(",")
    price = []
    items = []
    amount = []
    unit = []
    return render_template("drink.html", beverage = adminvalue, price = admin2value)
@app.route("/beverage_cranberry", methods = ["GET","POST"])
def beverage_cranberry():
    if request.method == "GET":  
        return render_template("beverage_cranberry.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_cranberry.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_cranberry.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 3.5
            price.append(total_price)
            items.append("Cranberry Juice")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_cranberry.html" , product = adminvalue, price = admin2value)
        
@app.route("/beverage_water", methods = ["GET","POST"])
def beverage_water():
    if request.method == "GET":  
        return render_template("beverage_water.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_water.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_water.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 1
            price.append(total_price)
            items.append("Water")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_water.html", product = adminvalue, price = admin2value)

@app.route("/beverage_oranage", methods = ["GET", "POST"])
def beverage_oranage():
    if request.method == "GET":  
        return render_template("beverage_oranage.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_oranage.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_oranage.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 3
            price.append(total_price)
            items.append("Oranage Juice")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_oranage.html", product = adminvalue, price = admin2value)
        
@app.route("/beverage_apple", methods = ["GET", "POST"])
def beverage_apple():
    if request.method == "GET":  
        return render_template("beverage_apple.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_apple.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_apple.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 3
            price.append(total_price)
            items.append("Apple Juice")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_apple.html", product = adminvalue, price = admin2value)

@app.route("/beverage_protein", methods = ["GET","POST"])
def beverage_protein():
    if request.method == "GET":  
        return render_template("beverage_protein.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_protein.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_protein.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 5
            price.append(total_price)
            items.append("Protein Milk")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_protein.html", product = adminvalue, price = admin2value)

@app.route("/beverage_cow", methods = ["GET", "POST"])
def beverage_cow():
    if request.method == "GET":  
        return render_template("beverage_cow.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_cow.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_cow.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 2.5
            price.append(total_price)
            items.append("Cows Milk")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_cow.html", product = adminvalue, price = admin2value)

@app.route("/beverage_oat", methods = ["GET", "POST"])
def beverage_oat():
    if request.method == "GET":  
        return render_template("beverage_oat.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_oat.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_oat.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 6
            price.append(total_price)
            items.append("Oat Milk")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_oat.html", product = adminvalue, price = admin2value)

@app.route("/beverage_lemonade", methods = ["GET","POST"])
def beverage_lemonade():
    if request.method == "GET":  
        return render_template("beverage_lemonade.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("beverage_lemonade.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("beverage_lemonade.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * 3
            price.append(total_price)
            items.append("Lemonade ")
            amount.append(quantity)
            unit.append("Gallons")

            file()
            return render_template("beverage_lemonade.html", product = adminvalue, price = admin2value)
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
