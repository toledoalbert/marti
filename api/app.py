from flask import *
import flask
from flask import jsonify
import tweepy
from flask.ext.jsonpify import jsonify

app = flask.Flask(__name__)

auth = tweepy.auth.OAuthHandler("Lr5Rq8fUegY0HiZwQAklQfRDw", "5iFM3HOGTbuM8incfI1SNujNHnaoMALTyqKL7f25zmIJWWaOaa", secure=True)
# auth.set_access_token("41089072-DUXKDDlEZNoA7mCfpQWGTVHcEEw4CNbPemJJs1ZpA", "o3SaoOZqvXG6kEeLIkt7YTBtv03iGLIDskj1SXk6RWWwv")
api = tweepy.API(auth)

@app.route("/")
def Hello():
    return "Hello Marti"

@app.route("/tweets")
def timeline():

    keywords = "cloudy OR sunny"
    results = tweepy.Cursor(api.search, q=keywords, lang="en", result_type="recent", geocode="37.781157,-122.398720,500mi").items(100)
    tweets = []

    for tweet in results:
        tweets.append(
                {
                    "text":tweet.text, 
                    "id":tweet.id
                    #, "loc": tweet.coordinates
                }
            )



    response = {"data":tweets}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)