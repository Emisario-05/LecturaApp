from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import generate_password_hash
import datetime 
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

Lectura = Flask(__name__)
db      = MySQL(Lectura)
adminSession = LoginManager(Lectura)

@adminSession.user_loader
def addUser(id):
    return ModelUser.get_by_id(db,id)

@Lectura.route('/')
def home():
    return render_template('home.html')

@Lectura.route('/signin',methods=['GET','PSOT0'])
def signin():
    if request.method == 'POST':
        usuario = User(0,None,request.form['correo'],request.form['clave'],None,None)
        usuarioAutenticado = ModelUser.signin(db,usuario)
        if usuarioAutenticado is not None:
            if usuarioAutenticado.clave:
                login_user(usuarioAutenticado)
                if usuarioAutenticado.perfil == 'A':
                    return render_template('admin.html')
                else:
                    return render_template ('user.html')
            else:
                return 'contraseña incorrecta'
        else:
            return 'usuario inexistente'
    else:
        return render_template('signin.html')

@Lectura.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
    Lectura.config.from_object(config['development'])
    Lectura.run(port=3300)