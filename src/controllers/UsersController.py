from flask import render_template

def create():
    return render_template('users/create.html')

def read():
    return "metodo de leitura e exibição dos dados"

def update():
    return "metodo de atualização dos dados"

def delete():
    return "metodo de delete dos dados"