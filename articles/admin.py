from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    """Inline to show comments on Article page"""

    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    """Admin for Articles"""

    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
