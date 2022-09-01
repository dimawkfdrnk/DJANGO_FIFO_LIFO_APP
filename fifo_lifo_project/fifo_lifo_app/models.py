from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count, F
from django.db import transaction




class HelpRequest(models.Model):
    full_name_petitioner = models.CharField(max_length=30)


class RequestThings(models.Model):
    number_request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE, null=True)
    name_thing = models.CharField(max_length=40)


class Donation(models.Model):
     full_name_donator = models.CharField(max_length=30)


class DonationThings(models.Model):
    number_donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)






# class Stocks(models.Model):
#     pass
#     name_stock = models.CharField(max_length=100)
#     vacancies = models.IntegerField(null=True, default=0)
#     occupied_places = models.IntegerField(null=True, default=0)
#
#     class Meta:
#         constraints = [
#             models.CheckConstraint(check=models.Q(vacancies__gte=F('occupied_places')), name="occupied_places_gte")
#         ]
#
#     def __str__(self):
#         return self.name_stock


# class Donation(models.Model):
#     pass
    # name = models.CharField(max_length=30)
    # amount = models.IntegerField()


# @receiver(post_save, sender=Donation)
# def func(sender, instance, **kwargs):
#     c = sender.objects.filter(stock_id=instance.stock_id, state="available")
#     Stocks.objects.select_for_update().filter(id=instance.stock_id).update(occupied_places=c.aggregate(Sum('amount'))['amount__sum'])





