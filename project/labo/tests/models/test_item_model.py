import pytest
from labo.models.item_model import Item

@pytest.fixture
def setUp():
    item = Item.objects.create(title='test_user1', content='password')
    item.save()


def test_user_model(setUp):
    assert Item.objects.filter(title='test_user1').count() == 1
    