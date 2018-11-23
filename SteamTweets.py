from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

#consumer key, consumer secret, access token, access secret.
consumerKey = 'fP20pja8Co8xYIdTmcexyU579'
consumerSecret = '5wFv34bF1Jc6n7oVRkBRsOgB9D6mtYME1YyE40kZf7MmvVmjHK'
accessToken = '606708487-NystO5Lt08aQYbGYgSb22SMOL1A77QOx3VLgfFlp'
accessTokenSecret = '1dZfIxdbYP6LEWPTcxHNyYcghXyisTOycWMNcCB2RyoSR'

class listener(StreamListener):

    def on_data(self, data):
        try:
            #print(data)

            tweet = data.split(',"text":')[1].split(',"source":')[0]
            print(tweet)



            saveThis = str(time.time())+"\t:"+tweet
            saveFile = open('TwitterSteam.txt', 'w')
            #saveFile.write(data)
            saveFile.write(saveThis)
            saveFile.write("\n")
            saveFile.close()
            return(True)

        except BaseException as e:
            print ('Failed Data Exception', str (e))
            time.sleep(5)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])



