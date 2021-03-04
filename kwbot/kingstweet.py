import time

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'kingsway'
number_of_tweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print('liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
