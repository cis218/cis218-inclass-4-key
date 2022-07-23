from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    """An Article"""

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_articles",
        blank=True,
    )

    def __str__(self):
        """Convert to string"""
        return self.title

    def get_absolute_url(self):
        """Get absolute url based on pk"""
        return reverse("article_detail", kwargs={"pk": self.pk})

    def get_like_url(self):
        """Get like url based on pk"""
        return reverse("article_like", kwargs={"pk": self.pk})


class Comment(models.Model):
    """A Comment"""

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self):
        """Convert to string"""
        return self.comment

    def get_absolute_url(self):
        return reverse("article_list")
