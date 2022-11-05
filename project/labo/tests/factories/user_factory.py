import factory
from faker import Faker

faker = Faker('ja_jp')

class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = 'labo.user'
        django_get_or_create = ()
        
    username = factory.Sequence(lambda x: f'{faker.name()}_{x}')