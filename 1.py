import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

###API ########################
ckey = "YZZwo7GpfrQXthMk2DzUOk1pj"
csecret = "SLVB2nDMZtM94R3k6L9BRuRleQSbr3wvt9U5HZ7Sem4geedRwk"
atoken = "2353244641-ArSJMSLFUgalKFwgHcxGJMBKDJilDton7lFO8OJ"
asecret = "556MIX1xYUd22D0oeVdoAO5xHY1LFFrlrs3XgIw0tRQd9"


#####################################
class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:

            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:Joel$2021*@localhost:5984/')  # ('##############')
try:
    db = server.create('hiroshima2021')
except:
    db = server['hiroshima2021']

'''===============LOCATIONS=============='''

twitterStream.filter(locations=[132.0318291328,33.9879199779,133.2465279422,34.7129148334])
# twitterStream.filter(track=['juegos olimpicos', 'Tokio 2020'])