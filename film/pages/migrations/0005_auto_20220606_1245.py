# Generated by Django 3.2.12 on 2022-06-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_episode_episode_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='movie_rating',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='release_year',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='running_time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
