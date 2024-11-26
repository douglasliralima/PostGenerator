from django.urls import path
from scraper.views.reddit import RedditScraperView
from scraper.views.twitter import TwitterScraperView

urlpatterns = [
    path('reddit/', RedditScraperView.as_view(), name='reddit_scraper'),
    path('twitter/', TwitterScraperView.as_view(), name='twitter_scraper'),
]
