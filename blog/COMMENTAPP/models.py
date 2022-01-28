from django.db import models
from django.contrib.auth.models import User
from POSTAPP.models import PostModel

class CommentModel(models.Model):
    Author      = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Yorumu Yazan Kişi")
    CreatedDate = models.DateTimeField(auto_now_add=True,verbose_name="Yorum Tarihi")
    CommentText = models.CharField(max_length=150,verbose_name="Yorum İçeriği")
    Post        = models.ForeignKey(PostModel,on_delete=models.CASCADE,verbose_name="Post",related_name="comments")
    Parent      = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    class Meta:
        db_table="Comments"
        verbose_name = "Yorum"
        verbose_name_plural="Yorumlar"
        ordering=("CreatedDate",)

    def children(self):
        return CommentModel.objects.filter(Parent=self)

    @property
    def any_children(self):
        return CommentModel.objects.filter(Parent=self).exists()

    def __str__(self):
        return str(self.CommentText)
