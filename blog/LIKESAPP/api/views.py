

from rest_framework.generics import ListAPIView
from LIKESAPP.models import LikesDislikesModel
from .serializers import LikesSerializer,DislikesSerializer

class LikesListAPIView(ListAPIView):
    serializer_class = LikesSerializer
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(Post__Slug=self.kwargs["Slug"],isLike=1)

class DislikesListAPIView(ListAPIView):
    serializer_class = DislikesSerializer
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(Post__Slug=self.kwargs["Slug"],isLike=0)

