# TWIT_TODO

## 前提環境
### 動作環境
- OS: Linux
- python: 3.6.4(多分3系なら動きます)

### 必要モジュール
- pyyaml
- twython

## ライブラリのインストール
1. `$ pip install pyyaml`
1. `$ pip install twython`

## 本体のインストール
1. `$ git clone https://github.com/tamago0224/twit_todo`
1. `$ cd twit_todo `
1. Twitterのcomsumer_keyとcomsumer_secret、access_toke、access_token_secretを[ここ](https://apps.twitter.com)でアプリを作成し、tw_config.ymlにセットする
1. Wunderlistのclient__idとaccess_tokenをさくせするために[ここ](https://developer.wunderlist.com/apps)でアプリを作成し、tw_config.ymlにセットする
1. `python twit_todo.py`
