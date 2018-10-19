from django.contrib import admin
from app.models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'abstract', 'image', 'content']
    list_filter = ['type']
admin.site.register(Article, ArticleAdmin)