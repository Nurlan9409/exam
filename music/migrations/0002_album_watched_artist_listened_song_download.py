# Generated by Django 5.0.4 on 2024-05-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='watched',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='listened',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='download',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
