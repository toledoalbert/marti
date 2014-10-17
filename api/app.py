from flask import *
import flask
from flask.ext.tweepy import Tweepy
from flask import jsonify
import tweepy

app = flask.Flask(__name__)

# app.config.setdefault('TWEEPY_CONSUMER_KEY', 'Lr5Rq8fUegY0HiZwQAklQfRDw')
# app.config.setdefault('TWEEPY_CONSUMER_SECRET', '5iFM3HOGTbuM8incfI1SNujNHnaoMALTyqKL7f25zmIJWWaOaa')
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', '41089072-DUXKDDlEZNoA7mCfpQWGTVHcEEw4CNbPemJJs1ZpA')
# app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', 'o3SaoOZqvXG6kEeLIkt7YTBtv03iGLIDskj1SXk6RWWwv')

# tweepy = Tweepy(app)

auth = tweepy.auth.OAuthHandler("Lr5Rq8fUegY0HiZwQAklQfRDw", "5iFM3HOGTbuM8incfI1SNujNHnaoMALTyqKL7f25zmIJWWaOaa", secure=True)
api = tweepy.API(auth)

@app.route("/")
def Hello():
    return "Hello Marti"

@app.route("/timeline")
def timeline():
    for tweet in api.home_timeline():
        print tweet.text

if __name__ == '__main__':
    app.run(debug=True)