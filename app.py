from flask import Flask,request, render_template

app = Flask(__name__)
### Routes
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return "We are ineuron"

@app.route("/operation", methods=["POST"])
def operation():
    if(request.method=="POST"):
        operation = request.form["operation"]
        Item_price1 = int(request.form["Item_price1"])
        Item_price2 = int(request.form["Item_price2"])
        Item_price3 = int(request.form["Item_price3"])
        Item_price4 = int(request.form["Item_price4"]) 
        total_sum =  Item_price1 + Item_price2 + Item_price3 + Item_price4

        if total_sum <= 1000:
            result = total_sum * 90/100
        elif total_sum > 1000 and total_sum <= 2000:
            total_sum = total_sum * 80/100
            result =  total_sum
        else:
            total_sum = total_sum * 70/100
            result = total_sum

            
        return render_template("result.html", result = result)


if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5000)
