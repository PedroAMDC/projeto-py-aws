from database import db
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    #Exemplo de tabela com 2 tuplas, registros
    #PK         HOMONIMOS       HOMONIMOS        CAMPO
    #CHAVE                                       UNICO
    #PRIMARIA
    #id           nome          sobrenome        EMAIL          
    #1            Pedro         Augusto          EMAIL                #tupla 1
    #2            Pedro         Martins          EMAIL                #tupla ou registro 2
    id = db.Column(db.Integer, primary_key=True)
    user_firstname = db.Column(db.String(25), nullable=False)
    user_lastname = db.Column(db.String(75), nullable=False)
    user_account = db.Column(db.String(25), unique=True, nullable=False)
    user_email = db.Column(db.String(255), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    user_datecreated = db.Column(db.DateTime(), nullable=False)
    user_is_active = db.Column(db.Boolean())
    user_is_delete = db.Column(db.Boolean())

    def __repr__(self):
        return f'<User "{self.user_account}">'
    
    def __init__(self, user_firstname, user_lastname, user_account, user_email, user_password, user_is_active, user_is_delete):
        self.user_firstname = user_firstname
        self.user_lastname = user_lastname
        self.user_account = user_account
        self.user_email = user_email
        self.user_password = generate_password_hash(user_password)
        self.user_datecreated = datetime.now() #.strftime("%d/%m/%y %H:%M:%S")
        self.user_is_active = user_is_active
        self.user_is_delete = user_is_delete