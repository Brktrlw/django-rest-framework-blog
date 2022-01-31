from django.urls import path
from .views import FavoritesListCreateAPIView
app_name="favorites"
urlpatterns = [
    path("list-create/",FavoritesListCreateAPIView.as_view(),name="favoritesListCreate")
]
