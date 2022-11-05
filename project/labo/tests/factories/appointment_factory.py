import factory
from faker import Faker

faker = Faker('ja_jp')

class AppointmentFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = 'labo.appointment'
        django_get_or_create = ()
        
    