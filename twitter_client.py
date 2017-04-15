from oauth import Oauth
import requests

BASE_URL = 'https://api.twitter.com/1.1/'


class TwitterClient:

    def __init__(self, consumer_key, consumer_secret):
        auth = Oauth(consumer_key, consumer_secret)
        self.auth_header = auth._get_auth_header()

    def _request_url(self, method, url, params={}, headers={}):
        headers = self.auth_header
        if method == 'POST':
            pass
        elif method == 'GET':
            response = requests.get(url, params=params, headers=headers)
            return response.json()

    def search_tag(self, hashtag, count=100):
        endpoint = 'search'
        request_data = 'tweets.json'
        url_pieces = [
            BASE_URL,
            endpoint,
            request_data
        ]

        url = '/'.join([piece.strip('/') for piece in url_pieces])
        params = {'q': hashtag, 'count': count}
        response = self._request_url('GET', url, params=params)

        return response
