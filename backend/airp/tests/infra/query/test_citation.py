from django.test import TestCase
from airp.models.citation import Citation
from accounts.models import CustomUser

class TestQueryCitation(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@airp.com",
            username="test"
            )
        self.citation = Citation.objects.create(
            user_id=self.user,
            citation="This is a citation",
            cite_comment="This is a comment",
            category=1,
            media=1,
            tag_ids="1,2,3",
            created_at="2021-01-01",
            updated_at="2021-01-01"
        )

    def test_citation(self):
        self.assertEqual(self.citation.user_id, self.user)
        self.assertEqual(self.citation.citation, "This is a citation")
        self.assertEqual(self.citation.cite_comment, "This is a comment")
        self.assertEqual(self.citation.category, 1)
        self.assertEqual(self.citation.media, 1)
        self.assertEqual(self.citation.tag_ids, "1,2,3")
        self.assertEqual(self.citation.created_at, "2021-01-01")
        self.assertEqual(self.citation.updated_at, "2021-01-01")
