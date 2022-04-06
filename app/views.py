from app import app

from flask import render_template
from flask import request

@app.route("/", methods=["GET"])
def index():
    return render_template('public/index.html', ip=request.remote_addr)

@app.route("/card/<name>", methods=['GET'])
def profile(name=None):
    return f'<h1 style="color: greenyellow">{name}</h1>'