from django.test import TestCase
from airp.models.citation import Citation
from accounts.models import CustomUser
from airp.infra.query.citation import CitationQuery
from airp.tests.fixture.factory.user import UserFactory
from airp.tests.fixture.factory.citation import CitationFactory

class TestQueryCitation(TestCase):

    def test_all(self):
        # data_setup
        user = UserFactory()
        citation = CitationFactory(user=user)

        # execute
        query = CitationQuery()
        result = query.all()
        
        # assersion
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['user_id'], user.id)
