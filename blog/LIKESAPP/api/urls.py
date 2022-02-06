
from django.urls import path
from .views import LikesListAPIView,CreateLikeAPIView

app_name="postlikes"
urlpatterns = [
    path('list/<Slug>',LikesListAPIView.as_view(),name="likeslist"),  # Bir postu beğenenlerin listesi
    path("like/<Slug>",CreateLikeAPIView.as_view(),name="like"),           # Bir postu Slug alanına göre beğenme ya da beğeniyi geri çekme
]
