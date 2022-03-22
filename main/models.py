from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("owner"))
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"))
    creation_date = models.DateTimeField(_("creattion date"), auto_now_add=True)
    upvotes = models.PositiveIntegerField(_("amount of upvotes"))
    slug = models.SlugField(_("slug"), unique=True)
    is_active = models.BooleanField(_("is active"), default=True)

    def __str__(self) -> str:
        return self.title[:20]

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-creation_date']


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name=_("article"),
        related_name="comments",
    )
    author_name = models.CharField(_("author name"), max_length=30)
    content = models.CharField(_("content"), max_length=255)
    creation_date = models.DateTimeField(_("creattion date"), auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author_name} -> {self.article.title[:20]}'

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
