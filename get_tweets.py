from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import csv

keyFile = open('keys', 'r')
consumer_key = keyFile.readline().rstrip()
consumer_secret = keyFile.readline().rstrip()
access_token = keyFile.readline().rstrip()
access_token_secret = keyFile.readline().rstrip()
keyFile.close()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

account_list = []
if (len(sys.argv) > 1):
    account_list = sys.argv[1:]
else:
    print("Please provide a list of usernames at the command line.")
    sys.exit(0)

if len(account_list) > 0:
    for target in account_list:
        print("Getting data for " + target)
        item = auth_api.get_user(screen_name=target)
        tweet_count = 0
        with open(target + ".csv", 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for status in Cursor(auth_api.user_timeline, screen_name=target).items():
                if not status.text.startswith("RT") and not status.text.startswith("@"):
                    if not "/" in status.text:
                        tweet_count += 1
                        print(status.text)
                        writer.writerow([status.text.rstrip()])

        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        print("description: " + item.description)
        print("tweet_count: " + str(tweet_count))
        print("friends_count: " + str(item.friends_count))
        print("followers_count: " + str(item.followers_count))
