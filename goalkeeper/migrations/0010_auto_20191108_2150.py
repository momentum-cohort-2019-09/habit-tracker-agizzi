# Generated by Django 2.2.7 on 2019-11-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalkeeper', '0009_auto_20191108_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='operator',
            field=models.CharField(choices=[('less than', 'less than'), ('more than', 'more than'), ('at least', 'at least'), ('at most', 'at most'), ('exactly', 'exactly')], max_length=10),
        ),
    ]
