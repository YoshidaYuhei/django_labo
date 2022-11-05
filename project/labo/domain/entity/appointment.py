
class AppointmentEntity:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, AppointmentEntity):
            return self.id == o.id
        return False
    id : int
    user_id: int # 購入したユーザー
    item_id: int # 購入したItem
    payment_method: str # 支払方法　コンビニ決済・クレジットカードなど
    payment_deadline: str # 支払期限
    schedule: str # Itemが実施される日時
    
    #TODO Itemの期日はscheduleより前でなければならない
    def is_schedule_before_item_period(item_period):
        pass