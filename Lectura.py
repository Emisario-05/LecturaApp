from flask import Flask, render_template, url_for, request, redirect
from flask import_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from datetime import datetime


Lectura = Flask(__name__)
db      = MySQL(__Lectura__)

@Lectura.route('/')
def home():
    return render_template('home.html')

@Lectura.route('/signup')
def signup():
    if request.metod == 'POST':
        nombre       = request.form['nombre']
        correo       = request.form['correo']
        clave        = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        fechareg     = datetime.now()

    return render_template('signup.html')

@Lectura.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
    Lectura.run(debug=True,port=3300)