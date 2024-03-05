# API 一覧

## Auth
### `POST auth/login`
* ログイン認証をする
#### In
    email : str
    password : str
#### Out
    type : str # Baerar
    access_token : str
    refresh_token : str

### `POST auth/signup`
* ユーザーアカウントを登録する
#### In
    email : str
    password : str
#### Out
    no_content

## User
### `GET users`
* 閲覧可能なのユーザーを取得する
#### Query Parameters
    gender : int
    per : int
    limit : int
#### Out
    List[UserCardOut]

### `GET users/:user_id`
* ユーザーの詳細情報を取得する
#### Path Parameters
    user_id : int
#### Out
    UserProfileOut

### `PUT users/:user_id`
* ユーザーのプロファイルを更新する
#### In
    UserProfileIn
#### Out
    no_content

### `DELETE users/:user_id`
* ユーザーアカウントを削除する
#### Path Parameters
    user_id : int
#### Out
    no_content

