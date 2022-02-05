from autoslug.settings import slugify
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils import timezone
from unidecode import unidecode
from django.core.validators import MaxValueValidator, MinValueValidator

class PostModel(models.Model):
    Author       = models.ForeignKey(User,on_delete=models.CASCADE)
    Title        = models.CharField(max_length=50)
    Content      = models.TextField()
    Draft        = models.BooleanField(default=False)
    CreatedDate  = models.DateTimeField(editable=False)
    ModifiedDate = models.DateTimeField(editable=False)
    Slug         = AutoSlugField(unique=True,max_length=150,editable=False,populate_from="Title")
    Image        = models.ImageField(upload_to="PostImages",null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.id:
            self.CreatedDate=timezone.now()
        self.ModifiedDate=timezone.now()
        self.Slug = slugify(unidecode(self.Title))
        return super(PostModel,self).save(*args,**kwargs)

    class Meta:
        db_table="Posts"
        verbose_name_plural="Postlar"
        verbose_name="Post"
        ordering=("CreatedDate",)

    def __str__(self):
        return self.Title

