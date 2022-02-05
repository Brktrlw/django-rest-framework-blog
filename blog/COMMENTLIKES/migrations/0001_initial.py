# Generated by Django 4.0.1 on 2022-02-05 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('COMMENTAPP', '0002_commentmodel_modifieddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLikesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='COMMENTAPP.commentmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Yorum Beğeni',
                'verbose_name_plural': 'Yorum Beğenileri',
                'db_table': 'CommentLikes',
            },
        ),
    ]