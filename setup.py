"""
    This is the main file to get started.
    Command line input are used to smooth
    user experience with the library.
"""

from secrets import CONSUMER_KEY, CONSUMER_SECRET
from twitter_client import TwitterClient
import click


client = TwitterClient(CONSUMER_KEY, CONSUMER_SECRET)
MIN_RETWEET = 1


@click.command()
@click.option('--input', prompt='Please enter hashtag you want to fetch')
def fetch_tweets(input):
    """
        This method fetches search response for
        given query input and displays it in
        user readable format into the command line
        itself.

        Args:
            input: string, possibly a word or hashtag
    """
    tweet_list = client.search(input)
    count = 1
    for tweet in tweet_list['statuses']:
        if is_valid_tweet(tweet):
            print "Tweet no. : ", count
            display_retweeted_tweet(tweet)
            print "#######################################################\n\n"
            count += 1


def display_retweeted_tweet(tweet):
    """
        Displays a tweets into user readable format,
        printing handle, tweet text and their retweets

        Args:
            tweet: tweet object
    """
    print tweet['user']['screen_name']
    print tweet['text']
    print "Retweets", tweet['retweet_count']


def is_valid_tweet(tweet):
    """
        Checks if this is a tweets we want to display.
        In our case a valid tweet is one which has atleast one retweet

        Args:
            tweet: tweet object

        Returns:
            True: if its a valid tweet to display
            False: if its a invalid tweet to display
    """
    return tweet['retweet_count'] >= MIN_RETWEET


if __name__ == '__main__':
    fetch_tweets()
