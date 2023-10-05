from flask import Flask, render_template, request

app = Flask(__name__)

def remainingcash(number1, number5):
    return number1+number5

def remaininggcash(number2, number4):
    return number2+number4

def newprofit(number3, number6):
    return number3+number6

@app.route("/", methods=["GET", "POST"])

def say():
    errors = []
    if request.method == "POST":
        number1 = None
        number2 = None
        number3 = None
        number4 = None
        number5 = None
        number6 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors.append("{!r} is not a number. \n".format(request.form["number1"]))
        try:
            number2 = float(request.form["number2"])
        except:
            errors.append("{!r} is not a number. \n".format(request.form["number2"]))
        try:
            number3 = float(request.form["number3"])
        except:
            errors.append("{!r} is not a number. \n".format(request.form["number3"]))
        try:
            number4 = float(request.form["number4"])
        except:
            errors.append("{!r} is not a number. \n".format(request.form["number4"]))
        try:
            number5 = float(request.form["number5"])
        except:
            errors.append("{!r} is not a number. \n".format(request.form["number5"]))
        try:
            number6 = float(request.form["number6"])
        except:
            errors.append("{!r} is not a number. \n".format(request.form["number6"]))

        if number1 is not None and number2 is not None and number3 is not None and number4 is not None and number5 is not None and number6 is not None:
            result1 = remainingcash(number1, number5)
            result2 = remaininggcash(number2, number4)
            result3 = newprofit(number3, number6)
            return render_template("calculation.html", number1=number1, number2=number2, number3=number3, number4=number4, number5=number5, number6=number6, result1=result1, result2=result2, result3=result3,)




    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)