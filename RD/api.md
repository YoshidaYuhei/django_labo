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
* ユーザーの一覧を取得する
#### Query Parameters
    gender : int
    per : int
    limit : int
#### Out
    List[UserCardOut]

### `GET users/profile/:user_id`
* 特定のユーザープロフィール情報を取得する
#### Path Parameters
    user_id : int
#### Out
    UserProfileOut

### `PUT users/profile/:user_id`
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

## Ranking
### `GET ranking/citations`
* 引用をいいねの付いた数順で表示する
#### Query Parameters
    per : int
    limit : int
#### Out
    List[Citation]

### `GET ranking/sources`
* 出典をいいねの付いた数順で表示する
#### Query Parameters
    per : int
    limit : int
#### Out
    List[Citation]

### `GET ranking/comments`

## Citation
### `GET citations`
### `POST citations/`
### `PUT citations/:citation_id`
### `DELETE citations/:citation_id`

## CiteReview
### `GET cite_reviews/`
### `POST cite_reviews/:citation_id`
### `PUT cite_reviews/:review_id`
### `DELETE cite_reviews/:review_id`

