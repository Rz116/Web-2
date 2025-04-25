from flask import Flask, request, render_template, redirect,url_for
import os
import main
app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])
def Produce (nameuser):
    global price, items, amount, unit, username, adminvalue,admin2value
    username = nameuser
    admin = open("Produce.txt", "r")
    adminvalue = admin.read().split(",")
    admin2 = open("Produceprices.txt", "r")
    admin2value = admin2.read().split(",")
    price = []
    items = []
    amount = []
    unit = []
    return render_template("produce.html", produce = adminvalue, price = admin2value)
@app.route("/produce_tomatoes", methods = ["GET","POST"])
def produce_tomatoes():
    if request.method == "GET":  
        return render_template("produce_tomatoes.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_tomatoes.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_tomatoes.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[0])
            price.append(total_price)
            items.append("Tomatoes")
            amount.append(quantity)
            unit.append("Lbs")

            file()
            return render_template("produce_tomatoes.html" , product = adminvalue, price = admin2value)
        
@app.route("/produce_broccoli", methods = ["GET","POST"])
def produce_broccoli():
    if request.method == "GET":  
        return render_template("produce_broccoli.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_broccoli.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_broccoli.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[1])
            price.append(total_price)
            items.append("Broccoli")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("produce_broccoli.html", product = adminvalue, price = admin2value)

@app.route("/produce_lettuce", methods = ["GET", "POST"])
def produce_lettuce():
    if request.method == "GET":  
        return render_template("produce_lettuce.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_lettuce.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_lettuce.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) *  float(admin2value[2])
            price.append(total_price)
            items.append("Lettuce")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("produce_lettuce.html", product = adminvalue, price = admin2value)
        
@app.route("/produce_eggplant", methods = ["GET", "POST"])
def produce_eggplant():
    if request.method == "GET":  
        return render_template("produce_eggplant.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_eggplant.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_eggplant.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[3])
            price.append(total_price)
            items.append("Eggplant")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("produce_eggplant.html", product = adminvalue, price = admin2value)

@app.route("/produce_apple", methods = ["GET","POST"])
def produce_apple():
    if request.method == "GET":  
        return render_template("produce_apple.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_apple.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_apple.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[4])
            price.append(total_price)
            items.append("Apples")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("produce_apple.html", product = adminvalue, price = admin2value)

@app.route("/produce_oranage", methods = ["GET", "POST"])
def produce_oranage():
    if request.method == "GET":  
        return render_template("produce_oranage.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_oranage.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_oranage.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[5])
            price.append(total_price)
            items.append("Oranages")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("produce_oranage.html", product = adminvalue, price = admin2value)

@app.route("/produce_lemons", methods = ["GET", "POST"])
def produce_lemons():
    if request.method == "GET":  
        return render_template("produce_lemons.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_lemons.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_lemons.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[6])
            price.append(total_price)
            items.append("Lemons")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("produce_lemons.html", product = adminvalue, price = admin2value)

@app.route("/produce_limes", methods = ["GET","POST"])
def produce_limes():
    if request.method == "GET":  
        return render_template("produce_limes.html", product = adminvalue, price = admin2value)
    else:
        quantity = request.form.get("quantity")
        if (quantity == ""):
            return render_template("produce_limes.html", product = adminvalue, price = admin2value)
        else:
            check = len(quantity)
            listcheck = list(quantity)
            for i in range(check):
                check2 = ord(listcheck[i])
                if(check2 < 49 or check2 > 57):
                    return render_template("produce_limes.html", product = adminvalue, price = admin2value)
            total_price = int(quantity) * float(admin2value[7])
            price.append(total_price)
            items.append("limes ")
            amount.append(quantity)
            unit.append("Pounds")

            file()
            return render_template("produce_limes.html", product = adminvalue, price = admin2value)
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
