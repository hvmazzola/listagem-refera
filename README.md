# Teste DEV Júnior Refera

Este repositório armazena o desafio da produção de uma aplicação web apresentado pela empresa Refera, visando avaliar o conhecimento técnico para a vaga de Dev Júnior. As funcionalidades implementadas foram as seguintes: listagem de usuários e cadastro de novos usuários.

A aplicação foi desenvolvida utilizando a liguagem de programação *Python3* e os *frameworks* [Flask](https://flask.palletsprojects.com/en/2.0.x/), [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/), [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/) e [WTForms](https://wtforms.readthedocs.io/en/3.0.x/).

  
- [Teste DEV Júnior Refera](#teste-dev-júnior-refera)
  - [Instalação](#instalação)
    - [Requisitos de Software](#requisitos-de-software)
    - [Executando a aplicação no *Linux* ou *MacOS*](#executando-a-aplicação-no-linux-ou-macos)
    - [Executando a aplicação no *Windows*](#executando-a-aplicação-no-windows)
  - [Rotas implementadas](#rotas-implementadas)

## Instalação

### Requisitos de Software

* *Python3*
* Sistema Operacional: *Linux*, *Windows* ou *MacOS*

### Executando a aplicação no *Linux* ou *MacOS*

Para executar a aplicação desenvolvida, siga os passos abaixo:

```bash
cd ~
git clone https://github.com/hvmazzola/teste-refera
cd teste-refera
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
:clap: Pronto! A aplicação estará rodando no endereço [`http://localhost:5000`](http://localhost:5000).

### Executando a aplicação no *Windows*

Para executar a aplicação desenvolvida, siga os passos abaixo:

```bash
git clone https://github.com/hvmazzola/teste-refera
cd teste-refera
python -m venv venv
cd venv/Scripts
activate.bat
cd ../..
pip install -r requirements.txt
python app.py
```
:clap: Pronto! A aplicação estará rodando no endereço [`http://localhost:5000`](http://localhost:5000).

## Rotas implementadas

| Rota | Método | Descrição |
| ---- | ---- | ---- |
| `/listar` | `GET` | Lista alguns dados dos usuários obtidos por meio da [API](https://jsonplaceholder.typicode.com/users) disponibilizada |
| `/adicionar` |  `GET` , `POST` |Apresenta um formulário de cadastro de um novo usuário |