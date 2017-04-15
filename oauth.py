import base64
import requests

BASE_URL = 'https://api.twitter.com/'


class Oauth:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.auth_type = 'Bearer'
        self.bearer_token = (base64.b64encode('{key}:{secret}'.format(
                             key=consumer_key,
                             secret=consumer_secret)))
        self.auth_token = self.__get_app_token()

    def __get_app_token(self):
        url = BASE_URL + 'oauth2/token'
        headers = {
            'Authorization': 'Basic ' + self.bearer_token,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        data = {'grant_type': 'client_credentials'}

        response = requests.post(url, headers=headers, data=data)
        return response.json().get('access_token')

    def _get_auth_header(self):
        return {'Authorization': self.auth_type + ' ' + self.auth_token}
