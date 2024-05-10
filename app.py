from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h2> Hello WOrld - Docker Flask Deployment Lab </h2> <hr/><p> Hello I am Sushma </p>"

app.run(host="0.0.0.0" , port = 5000)
