# Generated by Django 4.0.6 on 2022-09-01 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifo_lifo_app', '0011_remove_donationthings_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationthings',
            name='number_donation',
        ),
        migrations.RemoveField(
            model_name='requestthings',
            name='number_request',
        ),
        migrations.AddField(
            model_name='requestthings',
            name='number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifo_lifo_app.helprequest'),
        ),
    ]
