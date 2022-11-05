from labo.models import Item
from labo.infra.mapper import ItemMapper
from labo.domain.dto import ItemSearchDto

# QueryServiceはDBからQuerysetを取得するサービス
# QuerySetをDtoに変換する仕事はMapperが担当する
class ItemQueryService:
    
    def get_all_items(self):
        query_sets = Item.objects.all()
        dtos = [ItemSearchDto(x) for x in query_sets]
        return dtos