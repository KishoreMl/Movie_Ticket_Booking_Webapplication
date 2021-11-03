# Generated by Django 3.2 on 2021-10-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0005_auto_20211018_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheatreSeats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rowA', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='coverpic',
            field=models.ImageField(default=0, upload_to='Images'),
            preserve_default=False,
        ),
    ]
