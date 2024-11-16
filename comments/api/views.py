from django.db.models.expressions import result
from rest_framework import generics
from comments.api.serializer import CommentSerializer
from comments.models import Comment

import logging
LOGGER = logging.getLogger(__name__)

class AllCommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'commentType'
    lookup_url_kwarg = 'type'
    lookup_field_2 = 'relatedReference'
    lookup_url_kwarg_2 = 'reference'

    def get_queryset(self):
        try:
            LOGGER.info('Comment List filter by relatedReference and commentType inside get_queryset')
            comment_type = self.kwargs['type']
            reference = self.kwargs['reference']
            return Comment.objects.filter(relatedReference=reference, commentType=comment_type)
        except:
            LOGGER.error('Error in Comment List filter by relatedReference and commentType inside get_queryset')


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    LOGGER.info('Comment Create View')
    def perform_create(self, serializer):
        serializer.save(relatedReference=self.kwargs['reference'], commentType=self.kwargs['type'])
