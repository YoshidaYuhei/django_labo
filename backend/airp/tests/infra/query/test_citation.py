from django.test import TestCase
from airp.models.citation import Citation
from accounts.models import CustomUser
from airp.infra.query.citation import CitationQuery

class TestQueryCitation(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@airp.com",
            username="test"
            )
        self.citation = Citation.objects.create(
            user=self.user,
            citation="This is a citation",
            cite_comment="This is a comment",
            category=1,
            media=1,
            tag_ids="1,2,3",
            created_at="2021-01-01",
            updated_at="2021-01-01"
        )

    def test_all(self):
        query = CitationQuery()
        result = query.all()
        breakpoint()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['user_id'], self.user.id)
