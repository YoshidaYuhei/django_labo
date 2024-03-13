from typing import List
from django.core.serializers import serialize
from airp.models import Citation
from airp.domain.serializers.citation import CitationOut

class CitationQuery:
    def all(self) -> List[CitationOut]:
        citations = Citation.objects.all()
        data = [c.to_dict() for c in citations]
        ser = CitationOut(data=data, many=True)
        ser.is_valid()
        return ser.data