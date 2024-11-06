from flask import Flask, flash, render_template, url_for, request, redirect, session
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
                session['NombreU'] = usuarioAutenticado.nombre
                session['PerfilU'] = usuarioAutenticado.perfil
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

@Lectura.route('/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return redirect(url_for('home'))

@Lectura.route('/sUsuario', methods=['GET','POST'])
def sUsuario():
    sUsuario = db.connection.cursor()
    sUsuario.execute("SELECT * FROM usuario")
    u = sUsuario.fetchall()
    sUsuario.close()
    return render_template('usuarios.html',usuarios=u)

@Lectura.route('/iUsuario',methods=['GET', 'POST'])
def iUsuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    clave = request.form['clave']
    claveCifrada = generate_password_hash(clave)
    fechaReg = datetime.datetime.now()
    perfil = request.form['perfil']
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO usuario (nombre, correo, clave, fechareg, perfil) VALUES (%s, %s, %s, %s,%s)", (nombre, correo, claveCifrada, fechaReg, perfil))
    db.connection.commit()
    flash('usuario agregado')
    return redirect(url_for('sUsuario'))

@Lectura.route('/uUsuario/<int:id>', methods=['GET', 'POST'])
def uUsuario(id):
    nombre=request.form['nombre']
    correo=request.form['correo']
    clave=request.form['clave']
    perfil=request.form['perfil']
    actUsuario = db.connection.cursor()
    actUsuario.execute("UPDATE usuario SET nombre=%s,correo=%s,perfil=%s,clave=%s WHERE id=%s", (nombre,correo,perfil,clave,id))
    db.connection.commit()
    actUsuario.close()
    flash('usuario actualizado')
    return redirect(url_for('sUsuario'))

@Lectura.route('/dUsuario/<int:id>', methods=['GET','POST'])
def dUsuario(id):
    delUsuario= db.connection.cursor()
    delUsuario.execute("DELETE FROM usuario WHERE id=%s",(id,))
    db.connection.commit()
    flash('Este pendejo ya no existe')
    return redirect(url_for('sUsuario'))

@Lectura.route('/sLibros', methods=['GET','POST'])
def sLibros():
    sLibros = db.connection.cursor()
    sLibros.execute("SELECT * FROM Libros")
    lib = sLibros.fetchall()
    sLibros.close()
    if session['PerfilU'] == 'A':
        return render_template('libros.html', libros=lib)
    else:
        return render_template('usuario.html',usuarios=lib)

@Lectura.route('/iLibro',methods=['GET', 'POST'])
def iLibros():
    titulo = request.form['titulo']
    autor = request.form['autor']
    genero = request.form['genero']
    fecha_pub = request.form['fecha_pub']
    resumen = request.form['resumen']
    img = request.form['img']
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO usuario (titulo,autor,genero,fecha_pub,resumen,img) VALUES (%s,%s,%s,%s,%s,%s)", (titulo,autor,genero,fecha_pub,resumen,img))
    db.connection.commit()
    flash('libro agregado')
    return redirect(url_for('sLibros'))

@Lectura.route('/uLibros/<int:id>', methods=['GET', 'POST'])
def uLibros(id):
    titulo=request.form['titulo']
    autor=request.form['autor']
    genero=request.form['genero']
    fechapub=request.form['fechapub']
    resumen=request.form['resumen']
    img=request.form['img']
    actLibros = db.connection.cursor()
    actLibros.execute("UPDATE usuario SET titulo=%s,autor=%s,genero%s,fechapub=%s,resumen=%s,img=%s WHERE id=%s", (titulo,autor,genero,fechapub,resumen,img,id))
    db.connection.commit()
    actLibros.close()
    flash('Libro actualizado')
    return redirect(url_for('sLibros'))

@Lectura.route('/dLibros/<int:id>', methods=['GET','POST'])
def dLibros(id):
    delLibros= db.connection.cursor()
    delLibros.execute("DELETE FROM usuario WHERE id=%s",(id,))
    db.connection.commit()
    flash('Se borro el libro')
    return redirect(url_for('dLibros'))

if __name__ == "__main__":
    Lectura.config.from_object(config['development'])
    Lectura.run(port=3300)