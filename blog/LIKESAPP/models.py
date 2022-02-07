from django.contrib.auth.models import User
from django.db import models
from POSTAPP.models import PostModel
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from NOTIFICATIONAPP.models import ModelNotification

class PostLikesModel(models.Model):
    Post   = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name="likes")
    user   = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="PostLikes"
        verbose_name="Post Beğeni"
        verbose_name_plural="Post Beğenileri"


@receiver(post_save,sender=PostLikesModel)
def afterPostLike(sender,instance,created,*args,**kwargs):
    Article_Author = instance.Post.Author # Makale sahibi
    Like_User      = instance.user        # Beğenen Kullanıcı
    post           = instance.Post
    isLiked        = PostLikesModel.objects.filter(Post=post,user=Like_User).count()
    if isLiked==2: # zaten beğenmiş mi
        PostLikesModel.objects.filter(Post=post, user=Like_User).delete()
        # beğenmişse ve tekrar istek yapıyorsa beğeni bildirimini siliyoruz
        ModelNotification.objects.filter(user=Article_Author,post=post,re_user=Like_User).delete()
    else:
        if Article_Author!=Like_User:
            # eğer beğenmediyse bildirim oluşturuyoruz
            NotificationText = f"{post.Slug} gönderiniz {Like_User} tarafından beğenilmiştir."
            ModelNotification.objects.create(user=Article_Author,post=post,re_user=Like_User,NotificationText=NotificationText)


