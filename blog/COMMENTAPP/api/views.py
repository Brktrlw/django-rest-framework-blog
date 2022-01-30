from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveUpdateAPIView
from COMMENTAPP.models import CommentModel
from .serializers import CommentCreateSerializer,CommentListSerializers,CommentUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class CommentCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(Author=self.request.user)

class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializers
    def get_queryset(self):
        return CommentModel.objects.filter(Parent=None)

class CommentDeleteAPIView(DestroyAPIView):
    queryset = CommentModel.objects.all()
    lookup_field = "pk"
    serializer_class = CommentListSerializers

class CommentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CommentModel.objects.all()
    lookup_field = "pk"
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    def perform_update(self, serializer):
        serializer.save(Author=self.request.user)