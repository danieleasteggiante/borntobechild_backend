from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='sections')
    def __str__(self):
        return self.title