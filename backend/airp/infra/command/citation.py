from airp.models import Citation
from airp.domain.serializers.citation import CitationCreateIn

class CitationCommand:
    def create(self, create_in: CitationCreateIn) -> None:
        record = Citation(**create_in)
        record.save()
