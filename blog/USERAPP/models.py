from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProfileModel(models.Model):
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    twitter = models.CharField(max_length=100)

    class Meta:
        db_table="Profile"
        verbose_name="Profil"
        verbose_name_plural="Profil"

@receiver(post_save,sender=User)
def whenCreateUser(sender,**kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile=ProfileModel(user=user)
        user_profile.save()
    post_save.connect(whenCreateUser,sender=User)