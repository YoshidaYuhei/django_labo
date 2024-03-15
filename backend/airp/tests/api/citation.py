from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from airp.tests.fixture.factory.citation import CitationFactory

class CitationAPITestCase(APITestCase):
    def setUp(self):
        self.citations = CitationFactory.create_batch(5)

    def test_get_citations_all(self):
        url = reverse('citations-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.citations))