import GetOldTweets3 as got
import csv
import preprocessor as p ## to clean tweets

# listed some options that are available with GOT3
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Trump')\
                                           .setTopTweets(True)\
                                           .setSince("2020-07-01")\
                                           .setMaxTweets(20)
                                           ##.setUsername()
                                           ##.setNear()
                                           ##.setWithin()
                                           ##.setUntil()
tweet = got.manager.TweetManager.getTweets(tweetCriteria)

with open ('tweetsfile.csv', mode = 'w', encoding = "utf-8") as csv_file:
   csvWriter = csv.writer(csv_file)
   for tweets in tweet:
       ## clean the tweets (here I have chosen to include hashtags and mentions)
       p.set_options(p.OPT.URL, p.OPT.RESERVED, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER)
       clean_text = p.clean(str(tweets.text))
       csvWriter.writerow([clean_text])