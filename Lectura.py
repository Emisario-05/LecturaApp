from flask import Flask, render_template, url_for

RpgApp = Flask(__name__)

@RpgApp.route('/')

def home():
    return render_template('index.html')

if __name__ == "__main__":
    RpgApp.run(debug=True,port=3300)