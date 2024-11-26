from rest_framework.views import APIView
from rest_framework.response import Response
from scraper.services.getTwitterPosts import get_popular_tweets

class TwitterScraperView(APIView):
    def get(self, request):
        query = request.GET.get('query', 'meme')
        tweets = get_popular_tweets(query=query)
        return Response({"tweets": tweets})
