from django.db import models

# Create your models here.
from home.validator import validate_image_size

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', validators=[validate_image_size], blank=True, null=True)

    def __str__(self):
        return self.name


class Element(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', validators=[validate_image_size], blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name
