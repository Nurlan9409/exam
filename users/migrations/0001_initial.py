# Generated by Django 5.0.4 on 2024-04-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]
