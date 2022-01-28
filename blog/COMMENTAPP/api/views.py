from rest_framework.generics import CreateAPIView,ListAPIView
from COMMENTAPP.models import CommentModel
from .serializers import CommentCreateSerializer,CommentListSerializers

class CommentCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(Author=self.request.user)

class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializers
    def get_queryset(self):
        return CommentModel.objects.filter(Parent=None)