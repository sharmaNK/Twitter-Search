"""
    This is only user facing class of the Library.
    All the other files are abstract layers.

    All featured methods like search, get_tweets
    will be implemented in this class.
"""
from oauth import Oauth
from errors import (TwitterAuthException, TwitterSearchException,
                    TwitterException)
import requests

BASE_URL = 'https://api.twitter.com/1.1/'


class TwitterClient:
    """
        Args:
            consumer_key: API key provided by twitter when app is created
            consumer_secret: API secret provided by twitter when app is created
    """
    def __init__(self, consumer_key, consumer_secret):
        auth = Oauth(consumer_key, consumer_secret)
        self.auth_header = auth._get_auth_header()

    def _request_url(self, method, url, params={}):
        """
            This method makes actual call to twitter api
            and returns the response in json format

            NOTE: Only GET is implemented as search tweets is
            a GET method, but when required POST will be implemented
            here as well

            Args:
                method: GET/POST/PATCH
                url: api endpoint
                params: request parameters
        """
        headers = self.auth_header
        if method == 'POST':
            pass  # TODO
        elif method == 'GET':
            try:
                response = requests.get(url, params=params, headers=headers)
            except Exception:
                raise TwitterException

            if response.status_code == 401 or response.status_code == 403:
                raise TwitterAuthException

            if response.status_code != 200:
                raise TwitterException

            return response.json()

    def search(self, query, count=100):
        """
            Queries the Twitter API with a given query string

            Args:
                query: query string to search for in twitter API
                       like customer or #customer
                count: No of results to fetch

            Returns:
                response from twitter api in the json format

        """
        endpoint = 'search'
        request_data = 'tweets.json'
        url_pieces = [
            BASE_URL,
            endpoint,
            request_data
        ]

        url = '/'.join([piece.strip('/') for piece in url_pieces])
        params = {'q': query, 'count': count}
        try:
            response = self._request_url('GET', url, params=params)
        except Exception:
            raise TwitterSearchException

        return response
