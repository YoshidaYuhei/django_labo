from typing import List
from django.core.serializers import serialize
from airp.models import Citation
from airp.domain.serializers.citation import CitationOut

class CitationQuery:
    def all(self) -> List[CitationOut]:
        citations = Citation.objects.all()
        citations_list = [c.__dict__ for c in citations]
        for citation_dict in citations_list:
            citation_dict.pop('_state', None)  # モデルの内部状態を示す'_state'キーを削除
        ser = CitationOut(data=citations_list, many=True)
        ser.is_valid()
        return ser.data