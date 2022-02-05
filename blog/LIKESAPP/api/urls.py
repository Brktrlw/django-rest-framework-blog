
from django.urls import path
from .views import LikesListAPIView,CreateLikeAPIView

app_name="likesdislikes"
urlpatterns = [
    path('likeslist/<Slug>',LikesListAPIView.as_view()),  # Bir postu beğenenlerin listesi
    path("like/<Slug>",CreateLikeAPIView.as_view()),      # Bir postu Slug alanına göre beğenme ya da beğeniyi geri çekme
]
