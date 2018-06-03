from twitter import Api
import yaml

def get_api_key(yaml_file):
    with open(yaml_file) as file:
        yml_data = yaml.load(file)

    return yml_data

def tweet(api, message):
    api.PostUpdate(message) 

def main():
    data = get_api_key("tw_config.yml")
    api = Api(data['comsumer_key'],
            data['comsumer_secret'],
            data['access_token'],
            data['access_token_secret'])

    statuses = api.GetUserTimeline(api.VerifyCredentials().id)
    print([s.text for s in statuses])
    #tweet(api, 'This is Test Tweet.')


if __name__ == '__main__':
    main()
