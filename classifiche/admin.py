from django.contrib import admin

# Register your models here.
from classifiche.models import Category, Element

admin.site.register(Category)
admin.site.register(Element)