#name.py 9/20
from flask import Flask

app = Flask(__name__)

@app.route("/") #route decorator;
#if anyone reaches root directory of webpage, return this root route
#@app.route("/map") #allows <ip>/map to work as webpage.

@app.route("/")
def firstPg():
    return __name__ + "this is the first page" #return rather than print bc Flask

@app.route("/secondpg")
def secondPg():
    return __name__ + "this is the second page" #return rather than print bc Flask

@app.route("/thirdpg")
def thirdPg():
    return __name__ + "this is the third page" #return rather than print bc Flask

if __name__ == '__main__':
    app.run()
