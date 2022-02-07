from django.contrib.auth.models import User
from django.db import models
from COMMENTAPP.models import CommentModel
from django.db.models.signals import post_save
from django.dispatch import receiver

class CommentLikesModel(models.Model):
    Comment   = models.ForeignKey(CommentModel,on_delete=models.CASCADE,related_name="likes")
    user      = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="CommentLikes"
        verbose_name="Yorum Beğeni"
        verbose_name_plural="Yorum Beğenileri"
    def __str__(self):
        return self.user.username + " " + str(self.Comment.id)


@receiver(post_save,sender=CommentLikesModel)
def afterCommentLike(sender,instance,created,*args,**kwargs):
    comment   = instance.Comment
    LikedUser = instance.user
    isLiked = CommentLikesModel.objects.filter(user=LikedUser,Comment=comment).count()
    if isLiked==2:
        CommentLikesModel.objects.filter(user=LikedUser, Comment=comment).delete()
