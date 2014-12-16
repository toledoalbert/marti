from flask import *
import flask
from flask import jsonify
import tweepy
import re
from pymongo import Connection
# import tweetstream
# from flask.ext.jsonpify import jsonify

app = flask.Flask(__name__)

auth = tweepy.auth.OAuthHandler("Lr5Rq8fUegY0HiZwQAklQfRDw", "5iFM3HOGTbuM8incfI1SNujNHnaoMALTyqKL7f25zmIJWWaOaa", secure=True)
# auth.set_access_token("41089072-DUXKDDlEZNoA7mCfpQWGTVHcEEw4CNbPemJJs1ZpA", "o3SaoOZqvXG6kEeLIkt7YTBtv03iGLIDskj1SXk6RWWwv")
api = tweepy.API(auth)

#URL
@app.route("/")
def Hello():
   return "Hello Marti"


@app.route('/getTweets/<bagofwords>', defaults={'geocodes': None})
@app.route('/getTweets/<bagofwords>/<geocodes>')
def getTweets(bagofwords, geocodes):

    wordsArray=bagofwords.split('+')
    bagofwords=bagofwords.replace('+',' OR ' )

    print bagofwords

    #gecode Option 
    results = tweepy.Cursor(api.search, q=bagofwords, lang="en", result_type="recent", geocode=geocodes).items(500)
    
    tweets = []

    allWords = []

    cnt = {}

    for word in wordsArray:
        cnt[word] = 0

    maxWord = ""
    maxNum = 0

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
                }
            )

        words = tweet.text.split(' ')

        for word in words:
            allWords.append(word)

    for word in allWords:
        if word in cnt.keys():
            cnt[word] += 1

    for word in wordsArray:
        if cnt[word] > maxNum:
            maxWord = word
            maxNum = cnt[word]

    response = jsonify({"data":tweets, "maxWord":maxWord, "wordCount":cnt})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/getTweetsAND/<bagofwords>', defaults={'geocodes': None})
@app.route('/getTweetsAND/<bagofwords>/<geocodes>')
def getTweetsAND(bagofwords, geocodes):

    wordsArray=bagofwords.split('+')
    bagofwords=bagofwords.replace('+',' ' )

    print bagofwords

    #gecode Option 
    results = tweepy.Cursor(api.search, q=bagofwords, lang="en", result_type="recent", geocode=geocodes).items(500)
    
    tweets = []

    allWords = []

    cnt = {}

    for word in wordsArray:
        cnt[word] = 0

    maxWord = ""
    maxNum = 0

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
                }
            )

        words = tweet.text.split(' ')

        for word in words:
            allWords.append(word)

    for word in allWords:
        if word in cnt.keys():
            cnt[word] += 1

    for word in wordsArray:
        if cnt[word] > maxNum:
            maxWord = word
            maxNum = cnt[word]

    response = jsonify({"data":tweets, "maxWord":maxWord, "wordCount":cnt})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/matchTweets/<regex>')
def matchTweets(regex):
    results = tweepy.Cursor(api.search, q="a OR it OR you OR and", lang="en", result_type="recent", geocode=None).items(1000)

    tweets = []
    # regex = 'be'
    regex = regex.replace("\"", "")
    exp = re.compile(r'%s' % regex)

    for tweet in results:
        match = exp.match(tweet.text)
        if match:
            tweets.append({'text':tweet.text, 'id':tweet.id})

    # if len(tweets) < 100:
    #     results = tweepy.Cursor(api.search, q="a OR it OR you OR and", lang="en", result_type="recent", geocode=None).items(1000)
    #         tweets = []
    #         # regex = 'be'
    #         regex = regex.replace("\"", "")
    #         exp = re.compile(r'%s' % regex)

    #         for tweet in results:
    #             match = exp.match(tweet.text)
    #             if match:
    #                 tweets.append({'text':tweet.text, 'id':tweet.id})

    response = jsonify({"data":tweets})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/regexTest/<text>')
def decodeFromURL(text):

    # Use a database already created on mongolab 
    # server = 'ds063240.mongolab.com'
    # port = 63240
    # db_name = 'marti'
    # username = 'marti'
    # password = 'marti2014'

    # conn = Connection(server, port)

    # db = conn[db_name]

    # db.authenticate(username, password)

    # posts = db.a

    tweets = []

    # regex = re.compile('^@', re.IGNORECASE)
    # for post in posts.find({'text' : regex}):
    #     tweets.append(post)
    #     if len(tweets) > 500:
    #         break

    # tweets = []
    # regex = regex.replace("\"", "")
    # exp = re.compile(r'%s' % regex)

    # for tweet in results:
    #     match = exp.match(tweet.text)
    #     if match:
    #         tweets.append({'text':tweet.text, 'id':tweet.id})

    response = jsonify({"data":tweets})
    # response = jsonify()
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response









