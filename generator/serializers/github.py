from rest_framework import serializers

class GitHubRepoSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()
    description = serializers.CharField(allow_blank=True)
