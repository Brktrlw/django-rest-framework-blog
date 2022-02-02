from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProfileModel(models.Model):
    user    = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    twitter = models.CharField(max_length=100)

    class Meta:
        db_table="Profile"
        verbose_name="Profil"
        verbose_name_plural="Profil"

    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def whenCreateUser(sender,**kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile=ProfileModel(user=user)
        user_profile.save()
    post_save.connect(whenCreateUser,sender=User)