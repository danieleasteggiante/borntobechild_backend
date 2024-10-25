from rest_framework import generics

from blog.api.serializer import ArticleSimpleSerializer, ArticleDetailSerializer
from blog.models import Article


class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSimpleSerializer

    def get_queryset(self):
        # recuperare gli articoli in ordine decrescente da un certo punto in poi
        # esempio: /all/?from=10&limit=5 recupera gli articoli dal 10 al 5
        if 'from' not in self.kwargs or 'limit' not in self.kwargs:
            return Article.objects.all().order_by('-created_at')
        start = self.kwargs['from']
        end = self.kwargs['limit']
        return Article.objects.filter(id__gte=start).order_by('-created_at')[:start-end]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])