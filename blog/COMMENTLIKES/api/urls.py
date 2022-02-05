
from django.urls import path
from COMMENTLIKES.api.views import CommentLikesListAPIView,CommentLikesCreateAPIView

app_name="commentlikes"
urlpatterns = [
    path('list/<pk>',CommentLikesListAPIView.as_view(),name="likeslist"),  # Bir yorumu beğenenlerin listesi
    path("like/<pk>", CommentLikesCreateAPIView.as_view(), name="like"),         # Yorumu beğenme ya da beğeniyi geri çekme
]
