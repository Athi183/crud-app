from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__) #name of the flask app

@app.route("/")
def index():
    return "Testing 123"

if __name__=="__main__":
    app.run(debug=True)
