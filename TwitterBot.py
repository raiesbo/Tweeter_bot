import tweepy
from datetime import date
import json

# date setting
today = str(date.today())

# json data
with open('D:\\CODES\\reb_pss.json', 'r') as f:
    tw = json.load(f)

with open('arch_quotes2.json', 'r') as j:
    ar = json.load(j)

# twitter authentication information
auth = tweepy.OAuthHandler(tw["twitter"]["consumer_key"], tw["twitter"]["consumer_secret"])
auth.set_access_token(tw["twitter"]["access_token"], tw["twitter"]["access_token_secret"])

api = tweepy.API(auth)

for qu in ar.keys():
    if today == ar[f"{qu}"]["date"]:
        api.update_status("\"" + ar[f"{qu}"]["quote"] + "\"" + " - " + ar[f"{qu}"]["author"])
        print("The Tweet has been published.")
        break

