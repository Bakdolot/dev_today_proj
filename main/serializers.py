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
    slug = serializers.SlugField(required=True)
