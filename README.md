# TWIT_TODO
A script to be added to the TODO list of Wunderlist when tweet with a specified hash tag

## Install
### Install modules
```
$ pip install pyyaml
$ pip install twython
$ pip install requests requests_oauthlib
```

### Download this repository
`$ git clone https://github.com/tamago0224/twit_todo`

### Setting config file
#### Twitter setting
- First make a Twitter application [here](https://apps.twitter.com).
- Create Comsumer Key, Comsumer Secret, Access Token and Access Token Secret.
- Those value sets to tw_config.yml(tw_config.yml.sample change to tw_config.yml).
#### Wunderlist setting
- Second make a Wnderlist application [here](https://developer.wunderlist.com/apps).
- Create client id and access token.
- Those value sets to tw_config.yml(tw_config.yml.sample change to tw_config.yml).

### Run
`$ python twit_todo.py`
