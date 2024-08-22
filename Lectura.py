from flask import Flask

RpgApp = Flask(__name__)

@RpgApp.route('/')

def home():
    return '<h1> Hola pendejos </h1>'

if __name__ == "__main__":
    RpgApp.run(debug=True,port=3300)