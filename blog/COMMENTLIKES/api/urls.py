
from django.urls import path
from COMMENTLIKES.api.views import CommentLikesListAPIView

app_name="commentlikes"
urlpatterns = [
    path('list/<pk>',CommentLikesListAPIView.as_view(),name="likeslist"),  # Bir postu beğenenlerin listesi
]
