from app import app

from flask import render_template
from flask import request

@app.route("/", methods=["GET"])
def index():
    ip2 = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return render_template('public/index.html', ip=request.environ['REMOTE_ADDR'], ip2=ip2)

@app.route("/card/<name>", methods=['GET'])
def profile(name=None):
    return f'<h1 style="color: greenyellow">{name}</h1>'