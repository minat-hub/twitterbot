import tweepy
import time
from decouple import config

consumer_key = config("consumer_key")
consumer_secret = config("consumer_secret")
access_token = config("access_token")
access_secret = config("access_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print("Twitter bot which retweets")
user = api.me()
search = '#EndSARS'
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
