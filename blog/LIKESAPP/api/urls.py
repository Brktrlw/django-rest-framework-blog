
from django.urls import path
from .views import LikesListAPIView,DislikesListAPIView,LikeCreateAPIView,LikeDeleteAPIView

app_name="likesdislikes"
urlpatterns = [
    path('likeslist/<Slug>',LikesListAPIView.as_view()),                # Bir postu beğenenlerin listesi
    path('dislikeslist/<Slug>', DislikesListAPIView.as_view()),         # Bir postu beğenmeyenlerin listesi
    path("like/<Slug>",LikeCreateAPIView.as_view()),                    # Bir postu Slug alanına göre beğenme
    path("deletelike/<Post__Slug>",LikeDeleteAPIView.as_view()),        # Bir postu Slug alanına göre beğeniyi kaldırma
]
