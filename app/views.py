from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template('public/index.html')

@app.route("/card/<name>", methods=['GET'])
def profile(name=None):
    return f'<h1 style="color: greenyellow">{name}</h1>'