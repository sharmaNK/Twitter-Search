'''
    Oauth is most common authrization mechanism used by platforms
    like twitter, facebook, google to provide secure authorized
    access to system's API.
'''

import base64
import requests

BASE_URL = 'https://api.twitter.com/'


class Oauth:
    """
        Oauth class fetches auth token from twitter
        for given consumer key and secret.
        base64 encoding is used to encode auth credentials
        and hence create bearer_token

        Args:
            consumer_key: API key provided by twitter when app is created
            consumer_secret: API secret provided by twitter when app is created
    """
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.auth_type = 'Bearer'
        self.bearer_token = (base64.b64encode('{key}:{secret}'.format(
                             key=consumer_key,
                             secret=consumer_secret)))
        self.auth_token = self.__get_app_token()

    def __get_app_token(self):
        """
            This method is used to request auth token from twitter.

            Returns:
                access_token string
        """
        url = BASE_URL + 'oauth2/token'
        headers = {
            'Authorization': 'Basic ' + self.bearer_token,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        data = {'grant_type': 'client_credentials'}

        response = requests.post(url, headers=headers, data=data)
        return response.json().get('access_token')

    def _get_auth_header(self):
        """
            Returns:
                headers dict with authorization header evaluated
        """
        return {'Authorization': self.auth_type + ' ' + self.auth_token}
