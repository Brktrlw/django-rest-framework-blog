from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from FAVORITES.models import FavoritesModel
from .serializers import FavoritesListCreateAPISerializer
from .paginations import FavoritesPagination

class FavoritesListCreateAPIView(ListCreateAPIView):
    queryset = FavoritesModel.objects.all()
    serializer_class = FavoritesListCreateAPISerializer
    pagination_class = FavoritesPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset=FavoritesModel.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)