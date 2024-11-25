from flask import render_template, request, redirect, url_for
from flask_login import current_user
from src.models.UsersModel import User, db

def create():
    #VERIFICA SE VISITANTE VEIO DE UM FORMULARIO "POST"
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        account = request.form['account']
        password = request.form['password']
        user = User(
            user_firstname = firstname,
            user_lastname = lastname,
            user_email = email,
            user_account = account,
            user_password = password,
            user_is_active = 1,
            user_is_delete = 0
        )
        db.session.add(user)
        db.session.commit()
        # TO DO CRIAR PRERSISTENCIA DOS DADOS
        return redirect(url_for('app_routes.logout'))
    
    return render_template('users/create.html',
                           currentuser = current_user)

def read():
    return "metodo de leitura e exibição dos dados"

def update():
    return "metodo de atualização dos dados"

def delete():
    return "metodo de delete dos dados"