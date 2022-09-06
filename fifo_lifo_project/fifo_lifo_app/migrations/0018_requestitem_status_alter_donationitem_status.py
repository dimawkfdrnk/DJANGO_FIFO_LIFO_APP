# Generated by Django 4.0.6 on 2022-09-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifo_lifo_app', '0017_rename_donation_id_donationitem_donation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestitem',
            name='status',
            field=models.CharField(choices=[('Expects', 'Expects'), ('Received', 'Received')], default='Free', max_length=15),
        ),
        migrations.AlterField(
            model_name='donationitem',
            name='status',
            field=models.CharField(choices=[('Free', 'Free'), ('Given_away', 'Given_away')], default='Free', max_length=15),
        ),
    ]