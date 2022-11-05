import pytest
from labo.models import Item
from labo.tests.factories import ItemFactory
from labo.infra.query_service import ItemQueryService
from labo.domain.entity import ItemEntity
from labo.domain.dto import ItemSearchDto

@pytest.mark.django_db
def test_get_all_items():
    ItemFactory.create_batch(3)
    
    query_service = ItemQueryService()
    result = query_service.get_all_items()
    
    assert len(result) == 3
    assert isinstance(result[0], ItemSearchDto) 
    