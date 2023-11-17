from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


class BlogPostView(ListView):
    model = Post
    template_name = "home.html"


class BlogPostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogPostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["author", "title", "body"]


class BlogPostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogPostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/"
