from django.urls import path
from .views import BlogPostView, BlogPostDetail

urlpatterns = [
    path("", BlogPostView.as_view(), name="home"),
    path("post/<int:pk>/", BlogPostDetail.as_view(), name="post_detail"),
]
