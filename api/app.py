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
    '''
    geo_codesCapitals={
"Montgomery":"32.380120,-86.300629,100mi",
"Juneau":"58.299740,-134.406794,100mi",
"Phoenix":"33.448260,-112.075774,100mi",
"Little Rock":"34.748655,-92.274494,100mi",
"Sacramento":"38.579065,-121.491014,100mi",
"Denver":"39.740010,-104.992259,100mi",
"Hartford":"41.763325,-72.674069,100mi",
"Dover":"39.158035,-75.524734,100mi",
"Tallahassee":"30.439775,-84.280649,100mi",
"Atlanta":"33.748315,-84.391109,100mi",
"Honolulu":"21.304770,-157.857614,100mi",
"Boise":"43.606980,-116.193409,100mi",
"Springfield":"39.801055,-89.643604,100mi",
"Indianapolis":"39.766910,-86.149964,100mi",
"Des Moines":"41.589790,-93.615659,100mi",
"Topeka":"39.049285,-95.671184,100mi",
"Frankfort":"38.195070,-84.878694,100mi",
"Baton Rouge":"30.443345,-91.186994,100mi",
"Augusta":"44.318036,-69.776218,100mi",
"Annapolis":"38.976700,-76.489934,100mi",
"Boston":"42.358635,-71.056699,100mi",
"Lansing":"42.731940,-84.552249,100mi",
"Saint Paul":"44.943829,-93.093326,100mi",
"Jackson":"32.298690,-90.180489,100mi",
"Jefferson City":"38.577515,-92.177839,100mi",
"Helana":"46.589760,-112.021202,100mi",
"Lincoln":"40.813620,-96.707739,100mi",
"Carson City":"39.164885,-119.766999,100mi",
"Concord":"43.207250,-71.536604,100mi",
"Trenton":"40.217875,-74.759404,100mi",
"Santa Fe":"35.691543,-105.937406,100mi",
"Albany":"42.651445,-73.755254,100mi",
"Raleigh":"35.785510,-78.642669,100mi",
"Bismarck":"46.805372,-100.779334,100mi",
"Columbus":"39.961960,-83.002984,100mi",
"Oklahoma City":"35.472015,-97.520354,100mi",
"Salem":"44.933260,-123.043814,100mi",
"Harrisburg":"40.259865,-76.882230,100mi",
"Providence":"41.823875,-71.411994,100mi",
"Columbia":"33.998550,-81.045249,100mi",
"Pierre":"44.368924,-100.350158,100mi",
"Nashville":"36.167783,-86.778365,100mi",
"Austin":"30.267605,-97.742984,100mi",
"Salt Lake City":"40.759505,-111.888229,100mi",
"Montpelier":"44.260299,-72.576264,100mi",
"Richmond":"37.540700,-77.433654,100mi",
"Olympia":"47.039231,-122.891366,100mi",
"Charleston":"38.350195,-81.638989,100mi",
"Madison":"43.072950,-89.386694,100mi",
"Cheyenne":"41.134815,-104.821544,100mi"


    }
    



    geo_codes={

"AK": "61.3850,-152.2683,500mi",
"AL":"32.7990,-86.8073,500mi",
"AR":"34.9513,-92.3809,500mi",
"AS":"14.2417,-170.7197,500mi",
"AZ":"33.7712,-111.3877,500mi",
"CA":"36.1700,-119.7462,500mi",
"CO":"39.0646,-105.3272,500mi",
"CT":"41.5834,-72.7622,500mi",
"DC":"38.8964,-77.0262,500mi",
"DE":"39.3498,-75.5148,500mi",
"FL":"27.8333,-81.7170,500mi",
"GA":"32.9866,-83.6487,500mi",
"HI":"21.1098,-157.5311,500mi",
"IA":"42.0046,-93.2140,500mi",
"ID":"44.2394,-114.5103,500mi",
"IL":"40.3363,-89.0022,500mi",
"IN":"39.8647,-86.2604,500mi",
"KS":"38.5111,-96.8005,500mi",
"KY":"37.6690,-84.6514,500mi",
"LA":"31.1801,-91.8749,500mi",
"MA":"42.2373,-71.5314,500mi",
"MD":"39.0724,-76.7902,500mi",
"ME":"44.6074,-69.3977,500mi",
"MI":"43.3504,-84.5603,500mi",
"MN":"45.7326,-93.9196,500mi",
"MO":"38.4623,-92.3020,500mi",
"MP":"14.8058,145.5505,500mi",
"MS":"32.7673,-89.6812,500mi",
"MT":"46.9048,-110.3261,500mi",
"NC":"35.6411,-79.8431,500mi",
"ND":"47.5362,-99.7930,500mi",
"NE":"41.1289,-98.2883,500mi",
"NH":"43.4108,-71.5653,500mi",
"NJ":"40.3140,-74.5089,500mi",
"NM":"34.8375,-106.2371,500mi",
"NV":"38.4199,-117.1219,500mi",
"NY":"42.1497,-74.9384,500mi",
"OH":"40.3736,-82.7755,500mi",
"OK":"35.5376,-96.9247,500mi",
"OR":"44.5672,-122.1269,500mi",
"PA":"40.5773,-77.2640,500mi",
"PR":"18.2766,-66.3350,500mi",
"RI":"41.6772,-71.5101,500mi",
"SC":"33.8191,-80.9066,500mi",
"SD":"44.2853,-99.4632,500mi",
"TN":"35.7449,-86.7489,500mi",
"TX":"31.1060,-97.6475,500mi",
"UT":"40.1135,-111.8535,500mi",
"VA":"37.7680,-78.2057,200mi",
"VI":"18.0001,-64.8199,500mi",
"VT":"44.0407,-72.7093,500mi",
"WA":"47.3917,-121.5708,500mi",
"WI":"44.2563,-89.6385,500mi",
"WV":"38.4680,-80.9696,500mi",
"WY":"42.7475,-107.2085,500mi",

    }
    '''
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
