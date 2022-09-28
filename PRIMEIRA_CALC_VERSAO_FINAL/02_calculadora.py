#baixe tb o arquivo 02_runtests_calculadora.py

# leia as instruções lá

import re
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("home.html")

@app.route("/calc")
def exibe_calculadora():
    return render_template("calculadora.html")

@app.route("/resultado")
def resultado():
    operador=request.args['ope']
    a= int(request.args['a'])
    b= int(request.args['b'])
    if operador == 'mult':
        result= a*b
        return render_template("resultado.html", var=result)
    elif operador == 'soma':
        result= a+b
        return render_template("resultado.html", var=result)
    elif operador == 'sub':
        result= a-b
        return render_template("resultado.html", var=result)
    else:
        result= a/b
        return render_template("resultado.html", var=result)

app.run(debug=True)
