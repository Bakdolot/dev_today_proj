from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = 