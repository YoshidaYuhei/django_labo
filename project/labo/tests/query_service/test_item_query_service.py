import pytest
from labo.models import Item
from labo.tests.factories import ItemFactory
from labo.infra.query_service import ItemQueryService
from labo.domain.entity import ItemEntity
from labo.domain.dto import ItemSearchDto

@pytest.mark.django_db
def test_all():
    ItemFactory.create_batch(3)
    
    query_service = ItemQueryService()
    result = query_service.all()
    
    assert len(result) == 3
    assert isinstance(result[0], ItemSearchDto) 

@pytest.mark.django_db
def test_fetch():
    item = ItemFactory.create()
    
    query_service = ItemQueryService()
    result = query_service.fetch(item.id)
    
    assert result.id == item.id
    assert isinstance(result, ItemSearchDto) 
    