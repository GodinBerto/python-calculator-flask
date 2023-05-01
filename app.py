from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "godinberto"

from calculator_operation import calculator

@app.route('/')
def index():
    flash("0")
    return render_template("index.html")

@app.route('/cal' , methods=['POST'])
def cal():
    a = request.form['num1']
    b = request.form['num2']
    operation = request.form['operation']

    result = calculator(a, b, operation)
    flash(str(result)) 
    return render_template("index.html")
