import dataclasses
from django.db.models import QuerySet
from labo.models import Item
from django.forms.models import model_to_dict

@dataclasses.dataclass
class ItemSearchDto:
    
    id : int
    user_id: int # Itemの作成者・host
    title: str
    description: str 
    period: str # Itemが提供している期限
    category_id: int
    available_hours: str # 提供可能時間帯
    available_day_of_week: str # 提供可能曜日
    service_time: str # 販売する時間(30分単位)
    image_url: str
    sub_image_urls: str # 複数可能なのでJsonフォーマット
    area: str
    communication_style: str # 電話・対面・オンライン・メッセージ
    public: bool # 公開するしない

    def __eq__(self, o: object) -> bool:
            if isinstance(o, ItemSearchDto):
                return self.id == o.id
            return False
        
    def __init__(self, item) -> None:
        self.id = item.id
        self.user_id = item.user_id
        self.title = item.title
        self.description = item.description
        self.category_id = item.category_id
        self.period = item.period
        self.available_hours = item.available_hours
        self.available_day_of_week = item.available_day_of_week
        self.service_time = item.service_time
        self.image_url = item.image_url
        self.sub_image_urls = item.sub_image_urls
        self.area = item.area
        self.communication_style = item.communication_style
        self.public = item.public
    