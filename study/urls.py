from django.urls import path

from study.views.github import GitHubProjectsView
from study.views.helloWorld import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('github/<str:username>/', GitHubProjectsView.as_view(), name='github_projects'),
]
