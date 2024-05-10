from flask import flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h2> Hello WOrld - Docker Flask Deployment Lab </h2> <hr/>"

app.run(host="0.0.0.0" , port = 5000)
