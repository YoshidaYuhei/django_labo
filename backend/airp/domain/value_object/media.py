from airp.domain.value_object.abstract import BaseIntEnum


class Media(BaseIntEnum):
    BOOK = 1        # 本
    TREATISE = 2    # 論文
    MOVIE = 3       # 映画
    TV = 4          # テレビ
    WEB = 5         # WEB
    ARTICLE = 6     # 記事
    UNKNOWN = 99    # 不明
