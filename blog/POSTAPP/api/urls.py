from django.urls import path
from .views import PostListAPIView
urlpatterns = [
    path("list",PostListAPIView.as_view(),name="list")
]





