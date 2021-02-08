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
    print("Checking the timeline...")
    interacted = False
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        if tweet._json['user']['screen_name'] == "AviiWorkspace":
            if not tweet._json['favorited']:
                api.create_favorite(tweet._json['id'])
                print("Tweet #" +
                      str(tweet._json['id']) + " has been liked.")
                interacted = True
            if not tweet._json['retweeted']:
                api.retweet(tweet._json['id'])
                print("Tweet #" +
                      str(tweet._json['id']) + " has been retweeted!")
                interacted = True
    if not interacted:
        print("Nothing new...")
    else:
        interacted = False


# Greet user and run once on startup
print("Brian the Accounting Software Guy has awakened from his deep slumber.")
like_and_retweet()
print("Brian will check the feed again every couple of hours from now on.")

schedule.every(102).minutes.do(like_and_retweet)

while 1:
    schedule.run_pending()
    time.sleep(1)
