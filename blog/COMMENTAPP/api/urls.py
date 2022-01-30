
from django.urls import path
from .views import CommentCreateAPIView,CommentListAPIView,CommentDeleteAPIView,CommentUpdateAPIView
app_name="comment"

urlpatterns = [
    path("create",CommentCreateAPIView.as_view(),name="createComment"),
    path("list",CommentListAPIView.as_view(),name="listComments"),
    path("delete/<pk>", CommentDeleteAPIView.as_view(), name="deleteComment"),
    path("update/<pk>", CommentUpdateAPIView.as_view(), name="updateComment"),
]
