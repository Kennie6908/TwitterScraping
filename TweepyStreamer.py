import json
import tweepy

## create streamer class
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer key", 
    "consumer secret key")
auth.set_access_token("access token", 
    "access token secret")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

## call streamer class, use tweepy.Stream
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)

# use .filter and track to narrow down stream
stream.filter(track=["Trump"], languages=["en"])