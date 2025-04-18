from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from articles.models import Article, Comment


class ApiCommentDetailView(LoginRequiredMixin, View):
    """Comment Detail View"""

    def get(self, request, article_pk, comment_pk, *args, **kwargs):
        comment = Comment.objects.values().get(pk=comment_pk)
        return JsonResponse(comment, safe=False)


class ApiCommentListView(LoginRequiredMixin, View):
    """List of Comments for an Article"""

    def get(self, request, article_pk, *args, **kwargs):
        comments = list(Comment.objects.filter(article__id=article_pk).values())
        return JsonResponse(comments, safe=False)


class ApiArticleDetailView(LoginRequiredMixin, View):
    """Article Detail View"""

    def get(self, request, article_pk, *args, **kwargs):
        article = Article.objects.values().get(pk=article_pk)
        comments = list(Comment.objects.filter(article__id=article_pk).values())
        article["comments"] = comments
        return JsonResponse(article, safe=False)


class ApiArticleListView(LoginRequiredMixin, View):
    """List of Articles"""

    def get(self, request, *args, **kwargs):
        articles = list(Article.objects.values())
        return JsonResponse(articles, safe=False)
