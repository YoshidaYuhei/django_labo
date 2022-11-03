import pytest
from labo.models.user_model import CustomUser


@pytest.fixture()
def setUp():
    user = CustomUser.objects.create(username='test_user1', password='password')
    user.save()
    
@pytest.mark.django_db
def test_user_model():
    assert CustomUser.objects.filter(username='John Doe').count() == 1
        