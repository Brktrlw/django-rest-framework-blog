

from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from LIKESAPP.models import LikesDislikesModel
from .serializers import LikesDetailSerializer,LikeCreateSerializer

class LikesListAPIView(ListAPIView):
    serializer_class = LikesDetailSerializer
    def get_queryset(self):
        return LikesDislikesModel.objects.filter(Post__Slug=self.kwargs["Slug"])

class CreateLikeAPIView(CreateAPIView):
    queryset = LikesDislikesModel.objects.all()
    serializer_class = LikeCreateSerializer

    def perform_create(self, serializer):
        # Eğer kullanıcı beğendiyse beğeniyi geri alıyoruz,beğenmediyse bgönderiyi beğeniyoruz.
        _isLike = LikesDislikesModel.objects.filter(user=self.request.user,Post=self.request.data.get("Post")).exists()
        if _isLike==False:
            serializer.save(user=self.request.user)
        else:
            likeObject = LikesDislikesModel.objects.get(user=self.request.user,Post=self.request.data.get("Post"))
            likeObject.delete()








