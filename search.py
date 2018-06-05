import json
import tweepy
from auth import get_api


api = get_api()


def search(query, count):
    return[status for status in tweepy.Cursor(api.search, q=query).items(count)]
    
topic = input("Enter a topic: ")
number_of_tweets = int(input("Enter number: "))
tweets = search(topic, number_of_tweets)


for tweet in tweets:
    print(tweet.text)


