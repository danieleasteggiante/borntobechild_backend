
from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    commentType = models.CharField(max_length=100)
    relatedReference = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.author +' - '+ self.created.strftime('%Y-%m-%d %H:%M:%S') + ' - ' + self.commentType + ' - ' + self.relatedReference