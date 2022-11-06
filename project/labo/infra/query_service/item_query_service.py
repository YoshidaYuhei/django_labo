from labo.models import Item
from labo.infra.mapper import ItemMapper
from labo.domain.dto import ItemSearchDto


class ItemQueryService:
    
    def all(self) -> list[ItemSearchDto]:
        query_sets = Item.objects.all()
        return [ItemSearchDto(x) for x in query_sets]
    
    def fetch(self, item_id: int) -> ItemSearchDto:
        query_set = Item.objects.filter(id=item_id)
        return ItemSearchDto(query_set.first())
    
    def search(self, where: str) -> list[ItemSearchDto]:
        query_sets = Item.objects.filter(where=where)