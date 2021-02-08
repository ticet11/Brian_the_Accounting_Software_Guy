import tweepy
import os
from dotenv import load_dotenv
import schedule
import time

load_dotenv()

# Authentication Deets #
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Beginning Functionality #

def like_and_retweet():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        if tweet._json['user']['screen_name'] == "AviiWorkspace" and not tweet._json['favorited']:
            api.create_favorite(tweet._json['id'])
            api.retweet(tweet._json['id'])

schedule.every(102).minutes.do(like_and_retweet)

while 1:
    schedule.run_pending()
    time.sleep(1)