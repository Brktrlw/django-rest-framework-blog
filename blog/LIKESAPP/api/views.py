
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,CreateAPIView
from LIKESAPP.models import PostLikesModel
from .serializers import LikesDetailSerializer,LikeCreateSerializer
from NOTIFICATIONAPP.models import ModelNotification
from POSTAPP.models import PostModel

class LikesListAPIView(ListAPIView):
    serializer_class = LikesDetailSerializer
    def get_queryset(self):
        return PostLikesModel.objects.filter(Post__Slug=self.kwargs["Slug"])

class CreateLikeAPIView(CreateAPIView):
    queryset = PostLikesModel.objects.all()
    serializer_class = LikeCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "Post__Slug"

    def perform_create(self, serializer):
        post = PostModel.objects.get(Slug=self.kwargs["Slug"])
        serializer.save(user=self.request.user,Post=post)










