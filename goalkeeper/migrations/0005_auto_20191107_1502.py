# Generated by Django 2.2.7 on 2019-11-07 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goalkeeper', '0004_auto_20191107_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 7, 15, 2, 52, 873364, tzinfo=utc)),
        ),
    ]
