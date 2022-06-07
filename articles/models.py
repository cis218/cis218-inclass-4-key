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

    def __str__(self):
        """Convert to string"""
        return self.title

    def get_absolute_url(self):
        """Get absolute url based on pk"""
        return reverse("article_detail", kwargs={"pk": self.pk})
