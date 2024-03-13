from rest_framework import serializers

class BaseCitation(serializers.Serializer):
    user_id = serializers.IntegerField()
    citation = serializers.CharField()
    category = serializers.IntegerField()

class CitationOut(BaseCitation):
    cite_comment = serializers.CharField()
    media = serializers.IntegerField()
    tag_ids = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()