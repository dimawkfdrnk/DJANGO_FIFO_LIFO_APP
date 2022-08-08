from django.db import models


class Stocks(models.Model):
    name_stock = models.CharField(max_length=100)

    def __str__(self):
        return self.name_stock


class Donation(models.Model):
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    state = models.CharField(max_length=20,
                             choices=(
                                 ('available', 'available'),
                                 ('booked', 'booked'),
                                 ('requested', 'requested'),
                                 ('shipped', 'shipped')),
                             default='available'
                             )


class Donate(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    amount = models.IntegerField()
    issuing_time = models.DateTimeField()
    full_name_recipients = models.CharField(max_length=50)
