# Generated by Django 4.0.6 on 2022-09-12 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifo_lifo_app', '0027_remove_helprequest_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationitem',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifo_lifo_app.stocks'),
        ),
        migrations.AddField(
            model_name='requestitem',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifo_lifo_app.stocks'),
        ),
    ]