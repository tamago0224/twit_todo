import yaml
import json
from requests_oauthlib import OAuth2Session


class WunderlistAPI:
    def get_wunderlist_api_keys(self, yaml_file):
        with open(yaml_file) as y:
            yml_data = yaml.load(y)
        return yml_data['Wunderlist']

    def init_wunderlist(self):
        wunder_data = self.get_wunderlist_api_keys("tw_config.yml")
        self.client_id = wunder_data['client_id']
        self.access_token = wunder_data['access_token']
        url = 'https://a.wunderlist.com/api/v1/user'
        params = {}

        wunder = OAuth2Session()
        wunder.headers['X-Client-ID'] = self.client_id
        wunder.headers['X-Access-Token'] = self.access_token
        req = wunder.get(url, params=params)

        if req.status_code == 200:
            return wunder
        else:
            return None

    def show_list(self):
        url = 'https://a.wunderlist.com/api/v1/lists'
        params = {}
        req = self.wunder.get(url, params=params)

        if req.status_code == 200:
            lists = json.loads(req.text)
            for l in lists:
                print("ID: {}, TITLE: {}".format(l['id'], l['title']))
        else:
            print("Error: status code: %d, do not get todo list." % req.status_code)

    def add_task(self, title):
        url = 'https://a.wunderlist.com/api/v1/tasks'
        params = {
                "list_id": 355782822,
                "title": title,
                }

        self.wunder.post(url, json=params)
