from django.contrib.auth.models import User
from django.db import models
from COMMENTAPP.models import CommentModel


class CommentLikesModel(models.Model):
    Comment   = models.ForeignKey(CommentModel,on_delete=models.CASCADE,related_name="likes")
    user      = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="CommentLikes"
        verbose_name="Yorum Beğeni"
        verbose_name_plural="Yorum Beğenileri"
