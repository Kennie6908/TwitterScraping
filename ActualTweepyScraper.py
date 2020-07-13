import tweepy
import json ## Didn't end up using it, but can get json data from tweet
import pandas as pd 
import csv
import re #regular expression
from textblob import TextBlob ## for sentiment analysis
import string
import preprocessor as p ## for tweet cleaning
import time


auth = tweepy.OAuthHandler("consumer key", 
    "consumer secret key")
auth.set_access_token("access token", 
    "access token secret")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
    
def gettweets():
       ## this search uses tweepy.Cursor for larger tweet count, filters out retweets, english only, and uses extended tweet mode to get full tweet. 
   for tweet in tweepy.Cursor(api.search, q='Reckful -filter:retweets', lang="en", tweet_mode = 'extended').items(300):
        ## the following is necessary to get full tweet (.full_text), instead of being limited to 120 chars (tweepy default)
       try:
            stringtweet = tweet.retweeted_status.full_text
            numlikes = tweet.retweeted_status.favorite_count
            retweetedstatus = "True"
       except AttributeError:  # Not a Retweet
            stringtweet = tweet.full_text
            numlikes = tweet.favorite_count
            retweetedstatus = "False"
       
       # tweet preprocessor options, removes unnecessary characters. I chose to leave in hashtags and mentions, otherwise use p.OPT.HASHTAG and p.OPT.MENTION       
       p.set_options(p.OPT.URL, p.OPT.RESERVED, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER)
       clean_text = p.clean(stringtweet)
       
       #Creates a sentimenttweet object from Textblob module, which contains tuple (polarity, subjectivity). Accessed on line 40. 
       sentimenttweet = TextBlob(clean_text)
       
       csvWriter.writerow((clean_text, sentimenttweet.sentiment.polarity, sentimenttweet.sentiment.subjectivity, tweet.user.screen_name, tweet.user.location, numlikes, tweet.retweet_count, tweet.created_at))    

with open ('tweetsfile.csv', mode = 'w', encoding = "utf-8", newline = '') as csv_file:
   csvWriter = csv.writer(csv_file)
   ## writes headers, then calls our method gettweets. 
   csvWriter.writerow(("Text", "Polarity", "Subjectivity", "Username", "Location", "Likes", "Retweets", "Date Created"))
   gettweets()

