# Generated by Django 3.2 on 2021-10-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0004_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='theatre',
            name='location',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='theatre',
            name='time1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='time2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='time3',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='time4',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='time5',
            field=models.CharField(max_length=20),
        ),
    ]