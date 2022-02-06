from django.db import models
from django.contrib.auth.models import User
from POSTAPP.models import PostModel

class ModelNotification(models.Model):
    user             = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Kullanıcı",related_name="notifications")
    NotificationText = models.CharField(max_length=200,verbose_name="Bildirim İçeriği")
    post             = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    re_user          = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name        = "Bildirim"
        verbose_name_plural = "Bildirimler"
        db_table            = "Notifications"

    def __str__(self):
        return self.user.username + " " + self.NotificationText



