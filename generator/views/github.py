from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from generator.serializers.github import GitHubRepoSerializer

class GitHubProjectsView(APIView):
    def get(self, request, username):
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        
        if response.status_code == 200:
            repos = response.json()
            serialized_data = GitHubRepoSerializer(repos, many=True).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Failed to fetch repositories. Check the username."},
                status=response.status_code
            )
