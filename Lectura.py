from flask import Flask, flash, render_template, url_for, request, redirect
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

@Lectura.route('/admin')
def admin():
    return render_template('admin.html')

@Lectura.route('/user')
def user():
    return render_template('user.html')

@Lectura.route('/signin',methods=['GET','POST'])
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
                flash('Contraseña incorecta')
            return redirect(request.url)
        else:
            flash('Usuario inexistente')
            return redirect(request.url)
    else:
        return render_template('signin.html')

@Lectura.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrado = generate_password_hash(clave)
        fechaReg = datetime.datetime.now()
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg) VALUES (%s, %s, %s, %s)", (nombre, correo, claveCifrado, fechaReg))
        db.connection.commit()
        regUsuario.close ()
        return render_template('home.html')
    else:
        return render_template('signup.html')

@Lectura.route('/sigout',methods=['get','post'])
def sigout():
    logout_user()
    return redirect(url_for('home'))

@Lectura.route('/sUsuario', methods=['GET','POST'])
def sUsuario():
    sUsuario = db.connection.cursor()
    sUsuario.execute("SELECT * FROM usuario")
    u = sUsuario.fetchall()
    sUsuario.close()
    return render_template('usuarios.html',usuarios=u)

@Lectura.route('/iUsuario', methods=['GET','POST'])
def iUsuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    clave = request.form['clave']
    claveCifrado = generate_password_hash(clave)
    fechaReg = datetime.datetime.now()
    perfil = request.form['perfil']
    regUsuario = db.connection.cursor()
    regUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg) VALUES (%s, %s, %s, %s)", (nombre.upper(), correo, claveCifrado, fechaReg))
    db.connection.commit()
    return redirect(url_for('sUsuario'))


if __name__ == "__main__":
    Lectura.config.from_object(config['development'])
    Lectura.run(port=3300)