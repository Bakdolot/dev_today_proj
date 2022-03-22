from .models import Article


def reset_upvotes():
    Article.objects.all().update(upvotes=0)
