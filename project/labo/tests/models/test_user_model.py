import pytest
from labo.models.user_model import User


@pytest.fixture()
def setUp():
    user = User.objects.create(username='test_user1', password='password')
    user.save()
    
@pytest.mark.django_db
def test_user_model():
    assert User.objects.filter(username='John Doe').count() == 1
        