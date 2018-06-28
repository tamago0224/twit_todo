import yaml
import wunderpy2


def get_wunderlist_api_keys(yaml_file):
    with open(yaml_file) as y:
        yml_data = yaml.load(y)

    return yml_data['Wunderlist']


def setup(ACCESS_TOKEN, CLIENT_ID):
    wunderlist = wunderpy2.WunderApi()
    client = wunderlist.get_client(ACCESS_TOKEN, CLIENT_ID)

    return client


def add_task(wunderlist, task_title):
    task = wunderlist.create_task(355782822,task_title)


if __name__ == '__main__':
    data = get_wunderlist_api_keys("tw_config.yml")
    CLIENT_ID = data['client_id']
    ACCESS_TOKEN = data['access_token']
    wunderlist = setup(ACCESS_TOKEN, CLIENT_ID)
    add_task(wunderlist, "sample")
