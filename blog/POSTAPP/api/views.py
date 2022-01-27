from rest_framework.generics import ListAPIView,RetrieveAPIView
from POSTAPP.models import PostModel
from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'Slug'

