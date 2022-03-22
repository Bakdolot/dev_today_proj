from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (
    ArticleSerializer,
    ArticleListSerializer,
    CommentSerializer,
    AddUpvoteSerializer,
)
from .models import Article, Comment
from .permissions import IsOwner
from .utils import generate_slug


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.filter(is_active=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return super().get_serializer_class()
        if self.action == "add_upvote":
            return AddUpvoteSerializer
        return ArticleSerializer

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        user = self.request.user
        slug = generate_slug()
        serializer.save(owner=user, slug=slug)

    @action(["post"], detail=False)
    def add_upvote(self, request, *args, **kwargs):
        article = get_object_or_404(self.get_queryset(), slug=request.data["slug"])
        article.upvotes += 1
        article.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
