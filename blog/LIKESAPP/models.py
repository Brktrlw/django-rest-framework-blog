from django.contrib.auth.models import User
from django.db import models
from POSTAPP.models import PostModel


class PostLikesModel(models.Model):
    Post   = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name="likes")
    user   = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="PostLikes"
        verbose_name="Post Beğeni"
        verbose_name_plural="Post Beğenileri"

