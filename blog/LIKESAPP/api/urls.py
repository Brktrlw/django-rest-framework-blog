
from django.urls import path
from .views import LikesListAPIView,DislikesListAPIView,LikeCreateAPIView

app_name="likesdislikes"
urlpatterns = [
    path('likeslist/<Slug>',LikesListAPIView.as_view()),
    path('dislikeslist/<Slug>', DislikesListAPIView.as_view()),
    path("like/<Slug>",LikeCreateAPIView.as_view())
]
