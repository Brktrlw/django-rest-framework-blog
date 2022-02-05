

from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from LIKESAPP.models import LikesDislikesModel
from .serializers import LikesDislikeDetailSerializer,LikeCreateSerializer,LikesDeleteSerializer

class LikesListAPIView(ListAPIView):
    serializer_class = LikesDislikeDetailSerializer
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(Post__Slug=self.kwargs["Slug"],isLike=1)

class DislikesListAPIView(ListAPIView):
    serializer_class = LikesDislikeDetailSerializer
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(Post__Slug=self.kwargs["Slug"],isLike=0)

class LikeCreateAPIView(CreateAPIView):
    queryset = LikesDislikesModel.objects.all()
    serializer_class = LikeCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,isLike=1)

class LikeDeleteAPIView(DestroyAPIView):
    serializer_class = LikesDeleteSerializer
    lookup_field = "Post__Slug"
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(user=self.request.user,Post__Slug=self.kwargs["Post__Slug"])







