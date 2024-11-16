from django.urls import path

from comments.api.views import CommentList, AllCommentsView, CommentCreateView

urlpatterns = [
    path('<str:type>/<str:reference>/', CommentList.as_view(), name='comment_list_realated'),
    path('all', AllCommentsView.as_view(), name='all_comments'),
    path('<str:type>/<str:reference>/create/', CommentCreateView.as_view(), name='comment_create'),
]