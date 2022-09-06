# Generated by Django 4.0.6 on 2022-09-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifo_lifo_app', '0015_donationitem_requestitem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedRequest',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('fifo_lifo_app.helprequest',),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Close', 'Close')], default='Open', max_length=15),
        ),
    ]
