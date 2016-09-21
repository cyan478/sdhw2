#name.py 9/20
from flask import Flask

app = Flask(__name__)

@app.route("/") #route decorator;

@app.route("/")
def firstPg():
    return __name__ + "this is the first page" 

@app.route("/secondpg")
def secondPg():
    return __name__ + "this is the second page" 

@app.route("/thirdpg")
def thirdPg():
    return __name__ + "this is the third page" 

if __name__ == '__main__':
    app.run()
