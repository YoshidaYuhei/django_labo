from django.test import TestCase
from airp.models.citation import Citation
from accounts.models import CustomUser
from airp.infra.query.citation import CitationQuery
from airp.tests.fixture.factory.user import UserFactory
from airp.tests.fixture.factory.citation import CitationFactory

class TestQueryCitation(TestCase):
    def setUp(self):
        # Create a CitationQuery instance for use in the test cases
        self.query = CitationQuery()

    def test_all(self):
        # data_setup
        cite_count = 5
        user = UserFactory()
        citation = CitationFactory.create_batch(cite_count, user=user)

        # execute
        result = self.query.all()
        
        # assersion
        self.assertEqual(len(result), cite_count)
        self.assertEqual(result[0]['user_id'], user.id)

    def test_pick(self):
        # data_setup
        user = UserFactory()
        citation = CitationFactory(user=user)

        # execute
        result = self.query.pick(citation.id)
        
        # assersion
        self.assertEqual(result['user_id'], user.id)

    # def test_search(self):
    #     # data_setup
    #     user = UserFactory()
    #     citation = CitationFactory(user=user)

    #     # execute
    #     result = self.query.search(citation.citation)
        
    #     # assersion
    #     self.assertEqual(len(result), 1)
    #     self.assertEqual(result[0]['user_id'], user.id)
