from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register("articles", views.ArticleViewSet)
router.register("comment", views.CommentViewSet)

urlpatterns = router.urls
