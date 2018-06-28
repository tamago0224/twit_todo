import yaml
import tweepy
from wunderlist import setup, add_task, get_wunderlist_api_keys


def get_twitter_api_keys(yaml_file):
    with open(yaml_file) as y:
        yml_data = yaml.load(y)

    return yml_data['Twitter']


data = get_twitter_api_keys("tw_config.yml")
COMSUMER_KEY = data['comsumer_key']
COMSUMER_SECRET = data['comsumer_secret']
ACCESS_TOKEN_KEY = data['access_token']
ACCESS_TOKEN_SECRET = data['access_token_secret']
TARGET_HASHTAG = data['target_hashtag']
users = ['tamago_0224']
auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)


class MyTweetStream(tweepy.StreamListener):
    def on_status(self, status):
        data = get_wunderlist_api_keys("tw_config.yml")
        client_id = data['client_id']
        access_token = data['access_token']
        wunderls = setup(access_token, client_id)

        if status.user.screen_name in users:
            title = status.text.split()[0]
            print("added task: %s" % title)
            add_task(wunderls, title)

        return True

    def on_err(self, status_code):
        print('Got an error with statsu code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True


if __name__ == '__main__':
    myTweetStream = MyTweetStream()
    mystream = tweepy.Stream(auth, myTweetStream)
    mystream.filter(track=[TARGET_HASHTAG])
