from rest_framework.generics import CreateAPIView,ListAPIView
from COMMENTAPP.models import CommentModel
from .serializers import CommentCreateSerializer,CommentListSerializers
from rest_framework.permissions import IsAuthenticated

class CommentCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(Author=self.request.user)

class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializers
    def get_queryset(self):
        return CommentModel.objects.all()