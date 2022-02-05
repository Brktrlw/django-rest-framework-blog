
from rest_framework.generics import ListAPIView
from COMMENTLIKES.models import CommentLikesModel
from .serializers import CommentLikesListSerializer

class CommentLikesListAPIView(ListAPIView):
    serializer_class = CommentLikesListSerializer
    def get_queryset(self):
        return CommentLikesModel.objects.filter(Comment_id=self.kwargs["pk"])



