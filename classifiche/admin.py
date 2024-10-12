from django.contrib import admin

# Register your models here.
from classifiche.models import Category, Element, Comment

admin.site.register(Category)
admin.site.register(Element)
admin.site.register(Comment)