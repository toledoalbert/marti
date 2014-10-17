from flask import *
import flask
from flask.ext.tweepy import Tweepy
from flask import jsonify

app = flask.Flask(__name__)

app.config.setdefault('TWEEPY_CONSUMER_KEY', 'Lr5Rq8fUegY0HiZwQAklQfRDw')
app.config.setdefault('TWEEPY_CONSUMER_SECRET', '5iFM3HOGTbuM8incfI1SNujNHnaoMALTyqKL7f25zmIJWWaOaa')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', '41089072-DUXKDDlEZNoA7mCfpQWGTVHcEEw4CNbPemJJs1ZpA')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', 'o3SaoOZqvXG6kEeLIkt7YTBtv03iGLIDskj1SXk6RWWwv')

tweepy = Tweepy(app)


@app.route("/")
def Hello():
    return "Hello Marti"

@app.route("/timeline")
def timeline():
    api = tweepy.api
    tweets = api.public_timeline()
    for tweet in tweets:
        print tweet.text
        
    return "dasdasdasd"

if __name__ == '__main__':
    app.run()