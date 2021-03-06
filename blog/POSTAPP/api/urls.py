from django.urls import path
from .views import PostListAPIView,PostDetailAPIView,PostDeleteAPIView,PostUpdateAPIView,PostCreateAPIView
from django.views.decorators.cache import cache_page
app_name="post"

urlpatterns = [
    path("list/",cache_page(60*1)(PostListAPIView.as_view()),name="postList"),
    path("detail/<Slug>",PostDetailAPIView.as_view(),name="postDetail"),
    path("delete/<Slug>", PostDeleteAPIView.as_view(), name="postDelete"),
    path("update/<Slug>", PostUpdateAPIView.as_view(), name="postUpdate"),
    path("create/", PostCreateAPIView.as_view(), name="postCreate"),
]





