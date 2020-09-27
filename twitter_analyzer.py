import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor

import sys
import twitter_credentials
import numpy as np
import pandas as pd
import time

class TStreamer():
    
    # This class is used to stream and process live tweets
    def __init__(self):
        self.twitter_authenticator = TAuthentication()

    def stream_tweets(self, captured_tweets_filename, keyword_list):
        
        listener = StdOutTweetListener(captured_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter()
        stream = Stream(auth,listener)
        stream.filter(track = keyword_list)


class TAuthentication():

    # This class handles authentification for the Twitter API


    def authenticate_twitter(self):
        auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_KEY_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_KEY, twitter_credentials.ACCESS_KEY_SECRET)
        return auth

class StdOutTweetListener(StreamListener):

    # Class that prints out received tweets

    def __init__(self, captured_tweets_filename):
        self.captured_tweets_filename = captured_tweets_filename

    def on_data(self, data):

        try:
            print(data)
            with open(self.captured_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self,status):
        if status == 420:
            return False


if __name__ == "__main__":

    keyword_list = []
    print("\nWelcome to Sentimento!\nChoose one or more key words to track tweet sentiments on a topic in real time!\n")
    user_input = input("Enter a keyword or \'done\':")
    if(user_input == 'done'):
        print('No keyword entered, exiting program.')
        sys.exit

    while( user_input != 'done'):
        keyword_list += user_input
        user_input = input("Enter a keyword or \'done\':")

    user_time = input('\nHow long do you want to collect tweets for? (seconds)')

    captured_tweets_filename = "tweets.json"

    twitter_stream = TStreamer()
    twitter_stream.stream_tweets(captured_tweets_filename, keyword_list)

    time.sleep(user_time)
    sys.exit

        
    



