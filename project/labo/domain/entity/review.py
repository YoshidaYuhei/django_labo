class ReviewEntity:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, ReviewEntity):
            return self.id == o.id
        return False
    id: int
    item_id: int # 評価するItem
    appointment_id: int  
    score: int # 10段階評価
    comment: str 
    