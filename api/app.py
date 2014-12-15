from flask import *
import flask
from flask import jsonify
import tweepy
import re
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
    results = tweepy.Cursor(api.search, q="hello", lang="en", result_type="recent", geocode=None).items(1000)

    tweets = []
    # regex = 'be'
    regex = regex.replace("\"", "")
    exp = re.compile(r'%s' % regex)

    for tweet in results:
        match = exp.match(tweet.text)
        if match:
            tweets.append({'text':tweet.text, 'id':tweet.id})

    response = jsonify({"data":tweets})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/regexTest/text')
def decodeFromURL(text):

    vocab = {
        "$":        "%24",
        "%":        "%25",
        "&":        "%26",
        ":":        "%3A",
        ";":        "%3B",
        "<":        "%3C",
        "=":        "%3D",
        ">":        "%3E",
        "?":        "%3F",
        "@":        "%40",
        "[":        "%5B",
        r'\':       "%5C",
        "]":        "%5D",
        "^":        "%5E",
        "`":        "%60",
        "{":        "%7B",
        "|":        "%7C",
        "}":        "%7D",
        "~":        "%7E"    
    }

    # regex = "a\sc&=>:@"

    for key in vocab:
        text.replace(vocab[key], key)

    print text












