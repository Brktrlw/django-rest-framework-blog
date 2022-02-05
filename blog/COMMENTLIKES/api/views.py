
from rest_framework.generics import ListAPIView,CreateAPIView
from COMMENTLIKES.models import CommentLikesModel
from .serializers import CommentLikesListSerializer,CreateCommentLikeSerializer
from rest_framework.permissions import IsAuthenticated

class CommentLikesListAPIView(ListAPIView):
    serializer_class = CommentLikesListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return CommentLikesModel.objects.filter(Comment_id=self.kwargs["pk"])

class CommentLikesCreateAPIView(CreateAPIView):
    serializer_class   = CreateCommentLikeSerializer
    permission_classes = [IsAuthenticated]
    queryset = CommentLikesModel.objects.all()
    def perform_create(self, serializer):
        _isLike = CommentLikesModel.objects.filter(user=self.request.user, Comment=self.request.data.get("Comment")).exists()
        if _isLike:
            # Eğer beğeni varsa beğeniyi geri sildiğimiz kısım
            likeObject = CommentLikesModel.objects.get(user=self.request.user, Comment=self.request.data.get("Comment"))
            likeObject.delete()
        else:
            # Eğer beğeni yoksa beğeniyi oluşturduğumuz kısım
            serializer.save(user=self.request.user)

