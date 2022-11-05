import pytest
import factory
from labo.models.item_model import Item
from labo.tests.factories import ItemFactory


@pytest.mark.django_db
def test_get_all_items():
    ItemFactory.create(title='testuser')
    
    items = Item.objects.all()
    import pdb;pdb.set_trace()
    
    query_service = ItemQueryService()
    result = query_service.get_all_items()
    
    assert len(result) == 3
    assert result[0] is ItemDto