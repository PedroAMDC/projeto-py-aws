from flask import render_template, request
from flask_login import login_required
#from src.models.UsersModel import User, db
#from src.models.PostsModel import Posts

@login_required
def create():
    #VERIFICA SE VISITANTE VEIO DE UM FORMULARIO "POST"
    #if request.method == 'POST':
    #    firstname = request.form['firstname']
    #    email = request.form['email']
    #    account = request.form['account']
    #    password = request.form['password']
    #    user = User(
    #        user_firstname = firstname,
    #        user_lastname = lastname,
    #        user_email = email,
    #        user_account = account,
    #        user_password = password,
    #        user_is_active = 1,
    #        user_is_delete = 0
    #    )
    #    db.session.add(user)
    #    db.session.commit()
        # TO DO CRIAR PRERSISTENCIA DOS DADOS
    #    return "Usuário criado com sucesso"
    return "TO DO CRIAR UPLOAD E PERSISTÊNCIA DO POST"
    
    return render_template('posts/create.html')

def read():
    return "metodo de leitura e exibição dos dados"

def update():
    return "metodo de atualização dos dados"

def delete():
    return "metodo de delete dos dados"