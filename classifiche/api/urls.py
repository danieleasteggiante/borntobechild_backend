from django.urls import path

from classifiche.api.view import ElementDetailView, ElementAllView, CommentList, CategoryAllView, RankingView
from home.api.view import HomeView

urlpatterns = [
    path('element/<int:id>/', ElementDetailView.as_view(), name='classifiche_element'),
    path('element/all/', ElementAllView.as_view(), name='classifiche_element_all'),
    path('category/all/', CategoryAllView.as_view(), name='classifiche_category_all'),
    path('ranking/<str:slug>/', RankingView.as_view(), name='classifiche_ranking'),
    path('comment/<str:slug>/', CommentList.as_view(), name='classifiche_comment'),
]