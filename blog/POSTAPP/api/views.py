from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from POSTAPP.models import PostModel
from .serializers import PostSerializer,PostDetailSerializer,PostCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .paginations import PostPagination

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = PostModel.objects.filter(Draft=False)
        return queryset

#Detay sayfası işlemi
class PostDetailAPIView(RetrieveAPIView):
    queryset         = PostModel.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field     = 'Slug'

#Silme İşlemi
class PostDeleteAPIView(DestroyAPIView):
    queryset           = PostModel.objects.all()
    serializer_class   = PostSerializer
    permission_classes = [IsOwner]
    lookup_field       = 'Slug'

    def perform_destroy(self, instance):
        instance.delete()
#Güncelleme işlemi
class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset           = PostModel.objects.all()
    serializer_class   = PostCreateUpdateSerializer
    permission_classes = [IsOwner,IsAuthenticated]
    lookup_field       = 'Slug'

    def perform_update(self, serializer):
        serializer.save(Author=self.request.user)

#Create işlemi
class PostCreateAPIView(CreateAPIView):
    queryset           = PostModel.objects.all()
    serializer_class   = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(Author=self.request.user)