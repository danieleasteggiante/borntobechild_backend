from django.urls import path

from oauthgoogle.views import login_google

urlpatterns = [
    path('login/', login_google, name='blog_article_all'),
    path('print/', login_google, name='blog_article_all'),
]