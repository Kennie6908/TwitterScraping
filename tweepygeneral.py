import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer key", 
    "consumer secret key")
auth.set_access_token("access token", 
    "access token secret")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

## post a tweet
api.update_status("tweet text here")

## retrieve last 20 tweets in timeline
timeline = api.home_timeline()
for tweet in timeline:
    print(f" {tweet.user.name} said {tweet.text}")
 
## to look at a specific user
user = api.get_user("name here without @")
print(user.name)
print(user.description)
print(user.location)

##look at user last 20 followers
print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

##to add friend
api.create_friendship("username")

##to search tweets, can use count for more tweets, or look at api.cursor (example in actualtweepyscraper.py)
for tweet in api.search(q="Trump", lang="en", rpp=5):
    print(f"{tweet.user.name}:{tweet.text}")