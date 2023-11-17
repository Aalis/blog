from django.urls import path
from .views import (
    BlogPostView,
    BlogPostDetail,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)

urlpatterns = [
    path("post/delete/<int:pk>/", BlogPostDeleteView.as_view(), name="post_delete"),
    path("post/edit/<int:pk>/", BlogPostUpdateView.as_view(), name="post_edit"),
    path("post/new/", BlogPostCreateView.as_view(), name="post_new"),
    path("", BlogPostView.as_view(), name="home"),
    path("post/<int:pk>/", BlogPostDetail.as_view(), name="post_detail"),
]
