from rest_framework import generics

from classifiche.api.serializer import ElementSerializer, CommentSerializer, CategorySerializer
from classifiche.models import Element, Category, Comment


class ElementDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class ElementAllView(generics.ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class CategoryAllView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RankingView(generics.ListCreateAPIView):
    # per ordinare gli elementi in base al rank asc,
    # per ordine decrescente si usa '-rank'
    serializer_class = ElementSerializer
    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return Element.objects.filter(category=category).order_by('rank')

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return Comment.objects.filter(category=category).order_by('-created_at')