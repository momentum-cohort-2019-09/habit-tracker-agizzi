# Generated by Django 2.2.7 on 2019-11-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalkeeper', '0010_auto_20191108_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='units',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
