

from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from LIKESAPP.models import PostLikesModel
from .serializers import LikesDetailSerializer,LikeCreateSerializer

class LikesListAPIView(ListAPIView):
    serializer_class = LikesDetailSerializer
    def get_queryset(self):
        return PostLikesModel.objects.filter(Post__Slug=self.kwargs["Slug"])

class CreateLikeAPIView(CreateAPIView):
    queryset = PostLikesModel.objects.all()
    serializer_class = LikeCreateSerializer

    def perform_create(self, serializer):
        # Eğer kullanıcı beğendiyse beğeniyi geri alıyoruz,beğenmediyse bgönderiyi beğeniyoruz.
        _isLike = PostLikesModel.objects.filter(user=self.request.user,Post=self.request.data.get("Post")).exists()
        if _isLike==False:
            serializer.save(user=self.request.user)
        else:
            likeObject = PostLikesModel.objects.get(user=self.request.user,Post=self.request.data.get("Post"))
            likeObject.delete()








