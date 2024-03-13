import factory
import random
from django.utils import timezone
from factory.django import DjangoModelFactory
from airp.models import Citation
from airp.tests.fixture.factory.user import UserFactory
from airp.domain.value_object.media import Media

class CitationFactory(DjangoModelFactory):
    class Meta:
        model = Citation

    user = factory.SubFactory(UserFactory)
    citation = factory.Sequence(lambda n: f'This is a citation {n}')
    cite_comment = factory.Faker('text')
    category = factory.Faker('random_int')
    media = random.choice(list(Media.__members__.values())).value
    tag_ids="1,2,3"
    created_at = timezone.now()
    updated_at = timezone.now()
