import factory
from faker import Faker

faker = Faker('ja_jp')

class ItemFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = 'labo.item'
        django_get_or_create = ()
        
    title = factory.Sequence(lambda x: f'{faker.name()}_{x}')