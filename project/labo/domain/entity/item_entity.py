class ItemEntity:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, ItemEntity):
            return self.id == o.id
        return False
    
    id : int
    user_id: int # Itemの作成者・host
    title: str
    description: str 
    period: str # Itemが提供している期限
    category: int
    available_hours: str # 提供可能時間帯
    available_day_of_week: str # 提供可能曜日
    service_time: str # 販売する時間(30分単位)
    image_url: str
    sub_image_urls: str # 複数可能なのでJsonフォーマット
    area: str
    communication_style: str # 電話・対面・オンライン・メッセージ
    public: bool # 公開するしない
