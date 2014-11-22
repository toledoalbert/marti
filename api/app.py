from flask import *
import flask
from flask import jsonify
import tweepy
# from flask.ext.jsonpify import jsonify

app = flask.Flask(__name__)

auth = tweepy.auth.OAuthHandler("Lr5Rq8fUegY0HiZwQAklQfRDw", "5iFM3HOGTbuM8incfI1SNujNHnaoMALTyqKL7f25zmIJWWaOaa", secure=True)
# auth.set_access_token("41089072-DUXKDDlEZNoA7mCfpQWGTVHcEEw4CNbPemJJs1ZpA", "o3SaoOZqvXG6kEeLIkt7YTBtv03iGLIDskj1SXk6RWWwv")
api = tweepy.API(auth)

#URL
@app.route("/")
def Hello():
   return "Hello Marti"


@app.route('/<bagofwords>', defaults={'geocodes': None})
@app.route('/<bagofwords>/<geocodes>')
def getTweets(bagofwords, geocodes):

    wordsArray=bagofwords.split('+')
    bagofwords=bagofwords.replace('+',' OR ' )

    #gecode Option 
    results = tweepy.Cursor(api.search, q=bagofwords, lang="en", result_type="recent", geocode=geocodes).items(100)
    
    tweets = []

    for tweet in results:
        tweets.append(
                {
                    'text':tweet.text, 
                    'id':tweet.id,
                    'sentiment':'positive',
                    'time':'past',
                    'scores':[
                        {
                           'word':'sunny',
                           'score':20 

                            }
                     ]
                    #, "loc": tweet.coordinates
                }
            )



    response = jsonify({"data":tweets})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(debug=True)
