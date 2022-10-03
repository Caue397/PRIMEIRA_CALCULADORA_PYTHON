#baixe tb o arquivo 02_runtests_calculadora.py

# leia as instruções lá

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
    try:
        operador=request.args['ope']
        a= int(request.args['a'])
        b= int(request.args['b'])
    except ValueError:
        return f'Não é possível calcular estes valores!!'
    except KeyError:
        return f'Não foi enviado os parâmetros obrigatórios!!'
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
        try:
            result= a/b
        except ZeroDivisionError:
            return "Não é possível calcular!!"
        return render_template("resultado.html", var=result)
app.run(debug=True)
