import yaml
import json
from requests_oauthlib import OAuth2Session


def get_wunderlist_api_keys(yaml_file):
    with open(yaml_file) as y:
        yml_data = yaml.load(y)

    return yml_data['Wunderlist']


def setup():
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
        print("Auth Error: %d" % req.status_code)

    return wunderlist


def list_task(wunderlist):
    list_url = 'https://a.wunderlist.com/api/v1/lists'
    params = {}

    req = wunderlist.get(list_url, params=params)

    if req.status_code == 200:
        lists = json.load(req.text)
        for l in lists:
            print(l['id'], l['title'].encode('utf-8'))
    else:
        print("Error: %d" % req.status_code)


def add_task(wunderlist):
    add_url = 'https://a.wunderlist.com/api/v1/tasks'
    params = {
        "list_id": 1,
        "title": "テスト",
    }

    req = wunderlist.post(add_url, json=params)

    if req.status_code == 201:
        print("task add successfuly")
    else:
        print("task add failed: %d" % req.status_code)


if __name__ == '__main__':
    data = get_wunderlist_api_keys("tw_config.yml")
    CLIENT_ID = data['client_id']
    ACCESS_TOKEN = data['access_token']
    wunderlist = setup()
    add_task(wunderlist)
