from rest_framework.views import APIView
from rest_framework.response import Response
from scraper.services.getRedditPosts import get_popular_posts

class RedditScraperView(APIView):
    def get(self, request):
        subreddit = request.GET.get('subreddit', 'memes')
        memes = get_popular_posts(subreddit=subreddit)
        print('Post successfully loaded')
        return Response({"memes": memes})
