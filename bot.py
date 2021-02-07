import tweepy
import os
from dotenv import load_dotenv

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
public_tweets = api.home_timeline()
print (public_tweets[0]._json['user']['screen_name'])