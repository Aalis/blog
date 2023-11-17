from django.views.generic import ListView, DetailView
from .models import Post


class BlogPostView(ListView):
    model = Post
    template_name = "home.html"


class BlogPostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
