from django.db import transaction
from airp.infra.command.citation import CitationCommand
from airp.domain.serializers.citation import CitationCreateIn

class CitationService:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command = CitationCommand()
        
    def create(self, create_in: CitationCreateIn):
        with transaction.atomic():
            self.command.create(create_in)
        
        return True