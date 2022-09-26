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
    html = '''
    <style>
        div {
            justify-content:center;
            display:flex;
            height:600px;

        }

        #a, #b {
            border-radius:20px;
            text-align:center;
            margin:auto;
            width:130px;
            display:flex;
            height:30px;
           
        }

        .fatores {
            display:flex;
            justify-content:space-between;
            flex-direction:row;
            width:300px;
            text-align:center;
        }

        form {
            width:300px;
            height:390px;
            text-align:center;
            display:flex;
            flex-direction:column;
            justify-content:space-betwen;
            padding:30px;    
            font-family:cambria;
            font-size:16px;
        }
        button, label {
            display:block;
        }

        label {
            margin-top:15px;
        }

        button {
            margin-top: 30px;
            border-radius:20px;
            border:none;
            background-color:#F5CB5C;
            padding:7px;
            width:100px;
            font-family:cambria;
            font-size:14px;
        }

        button:hover {
            border: 2px solid black;
            cursor:pointer;
        }

        fieldset {
            border:2px solid black;
            border-radius:30px;
            height:480px;
            padding:0px;
            margin-top:70px;
            background-color:lightgrey;
        }

        legend {
            text-align:center;
            font-family:cambria;
            font-size:18px;
            background-color:lightgrey;
            border:2px solid black;
            border-radius:30px;
            padding:10px;
        }

        .comentario {
            text-align:center;
        }

        .botão {
            height:70px;
        }

    </style>
    <div>
        <fieldset>
        <legend>CALCULADORA</legend>
        <form action="/resultado">
        <div class='fatores'>
            <input type="text" name="a" id="a" placeholder='Número 1'> 
            <input type="text" name="b" id="b" placeholder='Número 2'>
        </div>
        <label for='mult'>Multiplicação:</label> 
        <input type="radio" name="ope" value="mult">
        <label for='div'>Divisão:</label> 
        <input type="radio" name="ope" value="div">
        <label for='soma'>Soma:</label> 
        <input type="radio" name="ope" value="soma">
        <label for='sub'>Subtração:</label> 
        <input type="radio" name="ope" value="sub">
        <div class='botão'>
            <button type="submit">Calcular</button>
        </div>
        </form>
        </fieldset>
    </div>

    <p class='comentario'>Implemente as operacoes! Teste com o arquivo runtests_calculadora.py</p>
    '''
    return html

'''
aqui, voce tem uma versão do resultado que sempre funciona. Nao delete.
Se precisar, copie ela de volta, embaixo
@app.route("/resultado")
def resultado():
    return ("os parametros preenchidos via form aparecem no dicionario request.args"+ 
            "<br>  Se voce acessou sem preencher o form, essa variavel é um dicionário" +
            "<br>  Vazio <br>" +  
            str(dict(request.args)))
'''


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

    

'''
@app.route("/resultado")
def resultado():
    return ("os parametros preenchidos via form aparecem no dicionario request.args"+ 
            "<br>  Se voce acessou sem preencher o form, essa variavel é um dicionário" +
            "<br>  Vazio <br>" +  
            str(dict(request.args)))
'''


app.run(debug=True)
