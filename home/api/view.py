from rest_framework import generics

from home.api.serializer import HomeSerializer, SectionSerializer
from home.models import Home, Section


class HomeView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    #permission_classes = [permissions.IsAuthenticated]
