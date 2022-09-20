# Generated by Django 4.0.6 on 2022-08-31 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifo_lifo_app', '0003_remove_helprequest_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='helprequest',
            name='order',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='requestthings',
            name='help_request',
        ),
        migrations.AddField(
            model_name='requestthings',
            name='help_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifo_lifo_app.helprequest'),
        ),
    ]
