from django.db import models

from home.validator import validate_image_size


# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='images/', validators=[validate_image_size])

    def __str__(self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    home = models.ForeignKey(Home, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return self.title


