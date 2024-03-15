from django.test import TestCase
from airp.models.citation import Citation
from accounts.models import CustomUser
from airp.infra.command.citation import CitationCommand
from airp.tests.fixture.factory.user import UserFactory
from airp.tests.fixture.factory.citation import CitationFactory
from airp.domain.serializers.citation import CitationCreateIn

class TestCommandCitation(TestCase):
    def setUp(self):
        self.command = CitationCommand()

    def test_create(self):
        # data_setup
        request = {
            'user_id': 1,
            'citation': 'test citation'
        }
        create_in = CitationCreateIn(request)

        # execute
        result = self.command.create(create_in)
        
        # assersion
        self.assertEqual(result, None)
        self.assertEqual(Citation.objects.all()[0]['user_id'], request['user_id'])
