from typing import Any
from django.db.models import QuerySet
from labo.domain.entity import ItemEntity

class ItemMapper:
    def __call__(self, query_sets: QuerySet, *args: Any, **kwds: Any) -> ItemEntity:
        import pdb;pdb.set_trace()
        
    