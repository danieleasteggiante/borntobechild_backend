from django.urls import path

from blog.api.view import ArticleList, ArticleDetail

urlpatterns = [
    path('all/', ArticleList.as_view(), name='blog_article_all'),
    path('<int:pk>/', ArticleDetail.as_view(), name='blog_article_detail'),
]