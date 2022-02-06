

from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
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

    def perform_create(self, serializer):
        # Eğer kullanıcı beğendiyse beğeniyi geri alıyoruz,beğenmediyse gönderiyi beğeniyoruz.
        _isLike = PostLikesModel.objects.filter(user=self.request.user,Post=self.request.data.get("Post")).exists()
        post    = PostModel.objects.get(id=self.request.data.get("Post"))
        if _isLike==False:
            serializer.save(user=self.request.user)
            if post.Author!=self.request.user:
                #Eğer kendi postunu beğenmiyorsa bildirim oluşur.
                Notifmessage = f"{post.Slug} postunuz {self.request.user.username} tarafından beğenilmiştir."
                ModelNotification.objects.create(user=post.Author,NotificationText=Notifmessage,post=post,re_user=self.request.user)
        else:
            try:
                notification=ModelNotification.objects.get(user=post.Author,post=post,re_user=self.request.user)
                notification.delete()
            except:
                pass
            likeObject = PostLikesModel.objects.get(user=self.request.user,Post=self.request.data.get("Post"))
            likeObject.delete()








