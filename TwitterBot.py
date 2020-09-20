import tweepy
import time
import json

# json data
with open('D:\\CODES\\reb_pss.json', 'r') as f:
    tw = json.load(f)

with open('arch_quotes.json', 'r') as f:
    arch = json.load(f)

# twitter authentication information
auth = tweepy.OAuthHandler(tw["twitter"]["consumer_key"], tw["twitter"]["consumer_secret"])
auth.set_access_token(tw["twitter"]["access_token"], tw["twitter"]["access_token_secret"])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)