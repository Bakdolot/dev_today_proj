from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from djoser.serializers import UserSerializer

from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["creation_date"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ["owner", "creation_date", "slug", "upvotes"]


class ArticleListSerializer(ArticleSerializer):
    comments = CommentSerializer(many=True)
    owner = UserSerializer()

    class Meta:
        model = Article
        fields = "__all__"


class AddUpvoteSerializer(serializers.Serializer):
    slug = serializers.SlugField()

    def validate_slug(self, slug):
        try:
            self.instance = Article.objects.get(slug=slug)
            return slug
        except Article.DoesNotExist:
            raise ValidationError(message=_("Article not found"))

    def add_upvote(self):
        article = self.instance
        article.upvotes += 1
        article.save()
