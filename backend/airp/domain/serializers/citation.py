from rest_framework import serializers

class BaseCitation(serializers.Serializer):
    user_id = serializers.IntegerField()
    citation = serializers.CharField()

class CitationOut(BaseCitation):
    cite_comment = serializers.CharField(required=False)
    media = serializers.IntegerField()
    tag_ids = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

class CitationCreateIn(BaseCitation):
    cite_comment = serializers.CharField(required=False)
    media = serializers.IntegerField(required=False)
    tag_ids = serializers.CharField()

class CitationUpdateIn(BaseCitation):
    cite_comment = serializers.CharField(required=False)
    media = serializers.IntegerField(required=False)
    tag_ids = serializers.CharField()
