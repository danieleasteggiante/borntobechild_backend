from django.urls import path
from home.api.view import HomeView

urlpatterns = [
    path('sections/', HomeView.as_view(), name='home'),
]