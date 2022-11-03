# git command
## git stash
### 退避してすぐに取り出す
* git stash
  git checkout してなにか作業、戻ってくる
  git stash pop 0

### clear
* git stash clear

### コンフリクトの解消
* git checkout master       masterブランチに移動
  git pull                  最新の状態を反映
  git checkout dev          作業ブランチに移動
  git merge origin master   masterブランチの更新を作業ブランチに反映→コンフリクト箇所を修正
  git add target_file       コンフリクトを修正したファイルをaddする
  git commit                コミット

### addの取り消し
* git reset HEAD