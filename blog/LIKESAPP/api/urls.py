
from django.urls import path
from .views import LikesListAPIView,DislikesListAPIView

app_name="likesdislikes"
urlpatterns = [
    path('likeslist/<Slug>',LikesListAPIView.as_view()),
    path('dislikeslist/<Slug>', DislikesListAPIView.as_view()),
]
