from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey= 'EQ7HX8v1R6SsbQJmEoRK8DchH'
csecret ='2IM5kaQUjJADP33gniWT0JAFD8qsfHIZKiR20t1JoJKA0VUZDr'
atoken= '2847679180-Gg3Nar8oOHvt8UCCIdyRZ6CYiVDT81eZ5sEHp8R'
asecret ='8pvNKkAgp4oMAzB9hCLpt5Pd0wwyG3FrsowxNqRNv4laG'

#Listener Class
class listener(StreamListener):
	
	def on_data(self, data):
		#trimming data
		tweet=data.split(',"text":"')[1].split('","source')[0]
		print tweet

		#print data
		return True

	def on_error(self, status):
		print status

#authorizes application
auth= OAuthHandler (ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream= Stream(auth, listener())
twitterStream.filter(track=["weather"])	