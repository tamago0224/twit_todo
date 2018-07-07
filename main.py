import yaml
import tweepy
import json
from requests_oauthlib import OAuth2Session


def get_twitter_api_keys(yaml_file):
    with open(yaml_file) as y:
        yml_data = yaml.load(y)

    return yml_data['Twitter']


def get_wunderlist_api_keys(yaml_file):
    with open(yaml_file) as y:
        yml_data = yaml.load(y)

    return yml_data['Wunderlist']


def init_wunderlist():
    wunder_data = get_wunderlist_api_keys("tw_config.yml")
    client_id = wunder_data['client_id']
    access_token = wunder_data['access_token']
    url = 'https://a.wunderlist.com/api/v1/user'
    params = {}

    wunder = OAuth2Session()
    wunder.headers['X-Client-ID'] = client_id
    wunder.headers['X-Access-Token'] = access_token
    req = wunder.get(url, params=params)

    if req.status_code == 200:
        return wunder
    else:
        return None


def show_list(wunder):
    url = 'https://a.wunderlist.com/api/v1/lists'
    params = {}
    req = wunder.get(url, params=params)

    if req.status_code == 200:
        lists = json.loads(req.text)
        for l in lists:
            print("ID: {}, TITLE: {}".format(l['id'], l['title']))
    else:
        print("Error: status code: %d, do not get todo list." % req.status_code)


def add_task(wunder, title):
    url = 'https://a.wunderlist.com/api/v1/tasks'
    params = {
            "list_id": 355782822,
            "title": title,
            }

    req = wunder.post(url, json=params)

    if req.status_code == 200:
        print("task '%s' add successfuly." % title)
    else:
        print("Error: task add failed")


class MyTweetStream(tweepy.StreamListener):
    def __init__(self, users):
        self.users = users
        self.wunder = init_wunderlist()
        pass

    def on_status(self, status):
        if status.user.screen_name in self.users:
            title = status.text.split()[0]
            add_task(self.wunder, title)

        return True

    def on_err(self, status_code):
        print('Got an error with statsu code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True


def main():
    data = get_twitter_api_keys("tw_config.yml")
    COMSUMER_KEY = data['comsumer_key']
    COMSUMER_SECRET = data['comsumer_secret']
    ACCESS_TOKEN_KEY = data['access_token']
    ACCESS_TOKEN_SECRET = data['access_token_secret']
    TARGET_HASHTAG = data['target_hashtag']
    users = ['tamago_0224']
    auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

    myTweetStream = MyTweetStream(users)
    mystream = tweepy.Stream(auth, myTweetStream)
    mystream.filter(track=[TARGET_HASHTAG])


if __name__ == '__main__':
    main()
