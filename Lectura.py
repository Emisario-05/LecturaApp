from flask import Flask, render_template, url_for

Lectura = Flask(__name__)

@Lectura.route('/')
def home():
    return render_template('home.html')

@Lectura.route('/signup')
def signup():
    return render_template('signup.html')

@Lectura.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == "__main__":
    Lectura.run(debug=True,port=3300)