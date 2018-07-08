import yaml
from twython import TwythonStreamer
from wunderlistAPI import WunderlistAPI


def get_twitter_api_keys(yaml_file):
    with open(yaml_file) as y:
        yml_data = yaml.load(y)

    return yml_data['Twitter']


class TwitStreamer(TwythonStreamer):
    def __init__(self, comsumer_key, comsumer_secret, access_token_key, access_token_secret, users):
        super().__init__(comsumer_key, comsumer_secret, access_token_key, access_token_secret)
        self.users = users
        self.wunderlist = WunderlistAPI()

    def on_success(self, data):
        print(data)
        print(data['screen_name'])

    def on_error(self, status_code, data):
        print("Error: %d" % status_code)


def main():

    data = get_twitter_api_keys("tw_config.yml")
    COMSUMER_KEY = data['comsumer_key']
    COMSUMER_SECRET = data['comsumer_secret']
    ACCESS_TOKEN_KEY = data['access_token']
    ACCESS_TOKEN_SECRET = data['access_token_secret']
    TARGET_HASHTAG = data['target_hashtag']
    print(TARGET_HASHTAG)
    TARGET_USERS = data['target_users']

    twitStreamer = TwitStreamer(COMSUMER_KEY, COMSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, TARGET_USERS)
    twitStreamer.statuses.filter(track=TARGET_HASHTAG)


if __name__ == '__main__':
    main()
