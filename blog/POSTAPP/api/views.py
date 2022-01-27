from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from POSTAPP.models import PostModel
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .permissions import IsOwner
#Tüm postlar
class PostListAPIView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

#Detay sayfası işlemi
class PostDetailAPIView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'Slug'

#Silme İşlemi
class PostDeleteAPIView(DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'Slug'

#Güncelleme işlemi
class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    lookup_field = 'Slug'

#Create işlemi
class PostCreateAPIView(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(Author=self.request.user)