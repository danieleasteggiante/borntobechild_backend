from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from blog.models import Article, Section

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        SectionInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Section)