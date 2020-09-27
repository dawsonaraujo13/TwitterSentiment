import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


class StdOutTweetListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self,status):
        print(status)


if __name__ == "__main__":

    listener = StdOutTweetListener()
    auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_KEY_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_KEY, twitter_credentials.ACCESS_KEY_SECRET)

    api = tweepy.API(auth)

    stream = Stream(auth,listener)

    stream.filter(track = ['AMD'])
        
    



