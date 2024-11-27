from django.urls import path
from scraper.views.reddit import RedditScraperView

urlpatterns = [
    path('reddit/', RedditScraperView.as_view(), name='reddit_scraper'),
]
