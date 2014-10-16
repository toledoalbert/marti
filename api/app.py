from flask import *

app = flask.Flask(__name__)
app.secret_key = "bricksquad"

@app.route("/")
def Hello():
    return "Hello Marti"

if __name__ == '__main__':
    app.run()