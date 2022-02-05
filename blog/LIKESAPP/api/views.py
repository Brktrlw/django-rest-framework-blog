

from rest_framework.generics import ListAPIView,CreateAPIView
from LIKESAPP.models import LikesDislikesModel
from .serializers import LikesSerializer,DislikesSerializer,LikeSerializer

class LikesListAPIView(ListAPIView):
    serializer_class = LikesSerializer
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(Post__Slug=self.kwargs["Slug"],isLike=1)

class DislikesListAPIView(ListAPIView):
    serializer_class = DislikesSerializer
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(Post__Slug=self.kwargs["Slug"],isLike=0)

class LikeCreateAPIView(CreateAPIView):
    queryset = LikesDislikesModel.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,isLike=1)






