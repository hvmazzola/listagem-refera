from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/consulta_api",methods=['GET'])
def consulta_api():
    resultado = requests.get("https://jsonplaceholder.typicode.com/users")
    return (str(resultado.text))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)