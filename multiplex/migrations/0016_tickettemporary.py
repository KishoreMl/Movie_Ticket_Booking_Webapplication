# Generated by Django 3.2 on 2021-11-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0015_auto_20211031_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketTemporary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketId', models.CharField(max_length=100)),
                ('movieName', models.CharField(max_length=100)),
                ('theatreName', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('seats', models.TextField()),
                ('totalTickets', models.IntegerField()),
                ('confee', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]