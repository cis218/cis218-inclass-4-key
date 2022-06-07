from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    """List of Articles"""

    model = Article
    template_name = "article_list.html"


class ArticleCreateView(CreateView):
    """Create Article"""

    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )


class ArticleDetailView(DetailView):
    """Detail of Article"""

    model = Article
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):
    """Update Article"""

    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView):
    """Delete View"""

    model = Article
    template_name: str = "article_delete.html"
    success_url = reverse_lazy("article_list")
