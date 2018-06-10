import requests

def get_outlook_api_keys(yaml_file):
    with open(yaml_file) as y:
        yaml_data = yaml.load(y)

    return yaml_data['OutlookTask']
