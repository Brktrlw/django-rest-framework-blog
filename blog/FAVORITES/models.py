from django.contrib.auth.models import User
from django.db import models
from POSTAPP.models import PostModel


class FavoritesModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Kullanıcı",related_name="favorites")
    Post = models.ForeignKey(PostModel,on_delete=models.CASCADE,verbose_name="Post")

    def __str__(self):
        return self.user.username + str(self.Post.Title)

    class Meta:
        verbose_name="Favori"
        db_table="Favorites"
        verbose_name_plural="Favoriler"