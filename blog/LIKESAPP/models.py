from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from POSTAPP.models import PostModel


class LikesDislikesModel(models.Model):
    Post   = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name="likes_and_dislikes")
    user   = models.ForeignKey(User,on_delete=models.CASCADE)
    isLike = models.IntegerField(null=True,blank=True,default=0,validators=[MaxValueValidator(1),MinValueValidator(0)])

    class Meta:
        db_table="LikesDislikes"
        verbose_name="Beğeni"
        verbose_name_plural="Beğeniler"
