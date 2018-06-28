import yaml
import json
from requests_oauthlib import OAuth2Session


def get_wunderlist_api_keys(yaml_file):
    with open(yaml_file) as y:
        yml_data = yaml.load(y)

    return yml_data['Wunderlist']


def setup():
    data = get_wunderlist_api_keys("tw_config.yml")
    CLIENT_ID = data['client_id']
    ACCESS_TOKEN = data['access_token']
    oauth_url = 'https://a.wunderlist.com/api/v1/user'
    params = {}

    wunderlist = OAuth2Session()
    wunderlist.headers['X-Client-ID'] = CLIENT_ID
    wunderlist.headers['X-Access-Token'] = ACCESS_TOKEN
    req = wunderlist.get(oauth_url, params=params)

    if req.status_code == 200:
        user = json.loads(req.text)
        print(user['name'])
    else:
        print("Error: %d" % req.status_code)


if __name__ == '__main__':
    setup()
