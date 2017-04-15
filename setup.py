from secrets import consumer_key, consumer_secret
from twitter_client import TwitterClient
import click


client = TwitterClient(consumer_key, consumer_secret)
MIN_RETWEET = 1


@click.command()
@click.option('--hashtag', prompt='Please enter hashtag you want to fetch')
def fetch_tweets(hashtag):
    """Simple program that greets NAME for a total of COUNT times."""
    tweet_list = client.search_tag(hashtag)
    count = 1
    for tweet in tweet_list['statuses']:
        if is_valid_tweet(tweet):
            print "Tweet no. : ", count
            display_retweeted_tweet(tweet)
            print_seprator()
            count += 1


def display_retweeted_tweet(tweet):
    print tweet['user']['screen_name']
    print tweet['text']
    print "Retweets", tweet['retweet_count']


def print_seprator():
    print "########################################################\n\n"


def is_valid_tweet(tweet):
    return tweet['retweet_count'] >= MIN_RETWEET


if __name__ == '__main__':
    fetch_tweets()
