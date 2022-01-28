
from django.contrib import admin
from django.urls import path,include
from .views import CommentCreateAPIView,CommentListAPIView
app_name="comment"

urlpatterns = [
    path("create",CommentCreateAPIView.as_view(),name="createComment"),
    path("list",CommentListAPIView.as_view(),name="listComments")
]
