# Generated by Django 3.2 on 2021-10-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0003_movie_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=0, upload_to='Images'),
            preserve_default=False,
        ),
    ]
