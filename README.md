# Tweepy and GoodOldTweets3

Before using Tweepy files, make sure you have a Twitter dev account and you take the consumer and access tokens and edit them in the files. 

4 files here. Running on Python 3.8

1. tweepygeneral is just a list of things you can do with tweepy. Mostly just a reference file for me, otherwise documentation can be found at http://docs.tweepy.org/en/latest/ . 

2. GOT3Scraper is the only GoodOldTweets3 file here. The benefit is that it looks through a lot more tweets than Tweepy, which is rate limited. However, it has very poor documentation. 
Tweepy seems to have more features from its access to a Twitter dev account, so GOT3 vs Tweepy is more quantity vs quality. Heads up, I use the tweet preprocessor module, which can be
downloaded at https://pypi.org/project/tweet-preprocessor/ . This returns a csv file. 

3. TweepyStreamer can listen to a desired key word using Tweepy.stream, and will print them out. Not much effort was put in here, future ideas can include using tweet preprocessor or live
sentiment analysis that flags tweets based on extreme polarity. !! This is a cool idea !! 
Heads up, this one might be buggy since I struggled with this one. 

4. ActualTweepyScraper is what I mostly focused on. It uses pandas, tweet preprocessor, and the textblob sentiment analysis modules, so have those ready for import. This will return a 
csv file, with all the tweets, the polarity and subjectivity score, location, username, likes, retweets, and date. All returned nicely with appropriate headers. 

All tweet processor cleaning uses options which remove unnecessary characters like emojis. However, I have intentionally left in hashtags and mentions from cleaning. To remove those, 
add p.OPT.MENTION and p.OPT.HASHTAG in the options for cleaning. 

Tweepy was not created by me, please check out the official Tweepy github at https://github.com/tweepy/tweepy and https://www.tweepy.org/ . 
