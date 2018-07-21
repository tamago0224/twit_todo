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
        client_id = wunder_data['client_id']
        access_token = wunder_data['access_token']
        url = 'https://a.wunderlist.com/api/v1/user'
        params = {}

        self.wunder = OAuth2Session()
        self.wunder.headers['X-Client-ID'] = client_id
        self.wunder.headers['X-Access-Token'] = access_token
        self.wunder.get(url, params=params)

    def chose_list(self, lists):
        if lists is None:
            print("Error: no list,")
            sys.exit(1)

        print("Chose list id for posting your tweet.")
        index = 1
        for l in lists:
            print("{}) {}.".format(index, l['title']))
            index += 1

        chose_index = int(input(">>"))
        list_id = lists[chose_index-1]['id']
        return list_id

    def get_list(self):
        url = 'https://a.wunderlist.com/api/v1/lists'
        params = {}
        req = self.wunder.get(url, params=params)
        lists = None

        if req.status_code == 200:
            lists = json.loads(req.text)
        else:
            print("Error: status code: %d, do not get todo list." % req.status_code)

        return lists

    def add_task(self, title, list_id):
        url = 'https://a.wunderlist.com/api/v1/tasks'
        params = {
                "list_id": list_id,
                "title": title,
                }

        self.wunder.post(url, json=params)
