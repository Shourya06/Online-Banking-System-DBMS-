from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/contactUs")
def contactUs():
    return render_template("contactUs.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/Customer_login")
def Customer_login():
    return render_template("Customer_login.html")

@app.route("/Customer_log_reg")
def Customer_log_reg():
    return render_template("Customer_log_reg.html")

@app.route("/Customer_register")
def Customer_register():
    return render_template("Customer_register.html")

@app.route("/Employee_login")
def Employee_login():
    return render_template("Employee_login.html")

@app.route("/Employee_log_reg")
def Employee_log_reg():
    return render_template("Employee_log_reg.html")

@app.route("/Employee_register")
def Employee_register():
    return render_template("Employee_register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/payments")
def payment():
    return render_template("payments.html")

@app.route("/card")
def card():
    return render_template("card.html")


if __name__ == "__main__":
    app.run(debug=True)