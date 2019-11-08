# Generated by Django 2.2.7 on 2019-11-08 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goalkeeper', '0013_auto_20191108_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
