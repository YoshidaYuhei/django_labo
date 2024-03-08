from rest_framework import serializers

class CitationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    citation = serializers.CharField()
    cite_comment = serializers.CharField()
    category = serializers.IntegerField()
    created_at = serializers.DateField()
    updated_at = serializers.DateField()
    media = serializers.IntegerField()
    tag_ids = serializers.CharField()