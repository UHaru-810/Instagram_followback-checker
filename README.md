# Instagram Followback Checker

Instagramのフォローバックされていないアカウントを表示し、csvに書き出すプログラム

<br>

使う意味も特にない

使い方
----
1. 各自InstagramのデータをJSONでリクエスト、ダウンロード
2. 同一フォルダ上に、"followers.json"と"following.json"を配置
3. 実行

<br>

- "followed.py": フォローバックされているアカウントをcsvに書き出し
- "not_followed.py": フォローバックされていないアカウントをcsvに書き出し

<br>

参考に
---
- "not_followed.py"ではフォローバックされてないアカウントプロフィールをChromeで表示する仕様なので注意
- 同じフォルダにcsvファイルが書き出されます