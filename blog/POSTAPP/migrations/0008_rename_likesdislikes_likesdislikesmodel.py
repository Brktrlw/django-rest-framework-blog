# Generated by Django 4.0.1 on 2022-02-05 17:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('POSTAPP', '0007_alter_likesdislikes_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikesDislikes',
            new_name='LikesDislikesModel',
        ),
    ]
