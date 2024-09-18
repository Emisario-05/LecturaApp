from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
import datetime 
from config import config


Lectura = Flask(__name__)
db      = MySQL(Lectura)

@Lectura.route('/')
def home():
    return render_template('home.html')

@Lectura.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        nombre       = request.form['nombre']
        correo       = request.form['correo']
        clave        = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg     = datetime.datetime.now()
        regUsuario   = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg) VALUES (%s, %s, %s, %s )", (nombre, correo, claveCifrada, fechareg))
        db.connection.commit()
        return render_template('home.html')
    else:
        return render_template('signup.html', methods = ['POST', 'GET'])

@Lectura.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
    Lectura.config.from_object(config['development'])
    Lectura.run(port=3300)