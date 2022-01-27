from flask import Flask, render_template, flash, redirect, url_for, request, session
import requests
from forms import Formulario
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link
import json

SECRET_KEY = 'secret'
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

boostrap = Bootstrap(app) 
nav = Nav()
nav.init_app(app)

@nav.navigation()
def menunavbar():
    menu = Navbar('Teste Refera')
    menu.items = [View('Home', 'index'), View('Adicionar usuario', 'adicionar')]
    return menu

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    f = Formulario()

    if request.method == 'POST':
        if f.validate_on_submit():
            flash("Save successfully")
          
            
    return render_template('formulario.html', title='Autenticação de usuários', form=f, menu=0)

@app.route("/consulta_api",methods=['GET'])
def consulta_api():
    resultado = requests.get("https://jsonplaceholder.typicode.com/users")
    return (str(resultado.text))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)