import json
import webbrowser
import csv
import subprocess
import os

# JSONファイル読み込み
with open('following.json') as json_open_following, open('followers.json') as json_open_followers:
    json_load_following = json.load(json_open_following)
    json_load_followers = json.load(json_open_followers)

# 各リスト初期化
list_following = []
list_followers = []
list_diff = [[]]

# Instagramのユーザーネーム取得
for json_key_following in json_load_following['relationships_following']:
    list_following.append(json_key_following['string_list_data'][0]['value'])
for json_key_followers in json_load_followers:
    list_followers.append(json_key_followers['string_list_data'][0]['value'])

# フォロー中とフォロワーの相違チェック
for elem in list_following:
    if elem not in list_followers:
        # URL作成
        url = 'https://instagram.com/' + elem
        # リストに追加
        list_diff.append([elem, url])
        # Chromeでフォローバックされていない各アカウントを表示
        webbrowser.get('chrome').open(url, new=0, autoraise=False)

#謎に1つ目の要素が空でできてしまうので削除(おそらくどこかが悪い)
del list_diff[0]

# csvファイルに書き込み
with open('not-followed.csv', 'w') as csv_open:
    csv_write = csv.writer(csv_open)
    csv_write.writerow(['ID ', 'URL'])
    csv_write.writerows(list_diff)

#csvファイルを開く(OS別)
try:
    if os.name == "nt":
        subprocess.Popen(['open', 'not-followed.csv'], shell=True)
    elif os.name == "posix":
        subprocess.Popen(['open', 'not-followed.csv'])
except:
    print("can't open csv file.")
