from rest_framework.generics import RetrieveUpdateAPIView,get_object_or_404,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer,UserCreateSerializer

class ProfileAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class   = UserSerializer
    queryset           = User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj      = get_object_or_404(queryset,id=self.request.user.id)
        return obj
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

