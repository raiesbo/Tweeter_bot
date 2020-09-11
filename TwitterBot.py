import Tweepy

# Authenticate to Twitter
# It's needed to register in the Tweepy web to access to the API and be able to use the modul
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api  = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet..text)

# Create a tweet
api.update_state("Hello Tweepy")