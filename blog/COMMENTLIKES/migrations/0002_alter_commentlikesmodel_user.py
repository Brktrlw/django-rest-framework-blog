# Generated by Django 4.0.1 on 2022-02-05 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('COMMENTLIKES', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentlikesmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
