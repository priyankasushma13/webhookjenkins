from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "<h2>Hello World - I am Sushma Priyanka flask deployment lab</h2><hr/>"

app.run(host="0.0.0.0",port=5000)
