import factory
from factory.django import DjangoModelFactory
from accounts.models import CustomUser

class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Faker('name')
    email = factory.Faker('email')