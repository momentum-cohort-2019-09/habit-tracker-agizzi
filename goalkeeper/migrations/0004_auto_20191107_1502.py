# Generated by Django 2.2.7 on 2019-11-07 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goalkeeper', '0003_auto_20191107_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='target',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 7, 15, 2, 36, 763365, tzinfo=utc)),
        ),
    ]