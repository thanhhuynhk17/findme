from app import app

from flask import render_template
from flask import request

@app.route("/", methods=["GET"])
def index():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
    return render_template('public/index.html', ip=ip.split(':')[0])

@app.route("/card/<name>", methods=['GET'])
def profile(name=None):
    return f'<h1 style="color: greenyellow">{name}</h1>'