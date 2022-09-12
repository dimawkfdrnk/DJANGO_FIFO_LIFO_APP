# Generated by Django 4.0.6 on 2022-09-11 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fifo_lifo_app', '0018_requestitem_status_alter_donationitem_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_stock', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='donationitem',
            name='status',
            field=models.CharField(choices=[('Free', 'Free'), ('Issued', 'Issued')], default='Free', max_length=15),
        ),
        migrations.AlterField(
            model_name='requestitem',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Close', 'Close')], default='Open', max_length=15),
        ),
        migrations.AddField(
            model_name='donation',
            name='stock_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifo_lifo_app.stocks'),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='stock_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fifo_lifo_app.stocks'),
        ),
    ]
