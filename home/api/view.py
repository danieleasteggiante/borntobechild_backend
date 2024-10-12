from rest_framework import generics

from home.api.serializer import HomeSerializer
from home.models import Home


class HomeView(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    #permission_classes = [permissions.IsAuthenticated]
