from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count, F
from django.db import transaction


# class Stocks(models.Model):
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



class HelpRequest(models.Model):
    full_name_petitioner = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices= (('Open', 'Open'), ('Close', 'Close')), default='Open')
    # stock_id = models.ForeignKey(Stocks, on_delete=models.CASCADE, null=True)



class Donation(models.Model):
    full_name_donator = models.CharField(max_length=50)
    # stock_id = models.ForeignKey(Stocks, on_delete=models.CASCADE, null=True)



class ItemDescription(models.Model):
    name_item = models.CharField(max_length=50)
    # amount = models.IntegerField(null=True, default=0)


    class Meta:
        abstract = True



class DonationItem(ItemDescription):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=15, choices=(('Free', 'Free'), ('Issued', 'Issued')), default='Free')


class RequestItem(ItemDescription):
    request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=15, choices=(('Open', 'Open'), ('Close', 'Close')), default='Open')


class ManagerHelpRequest(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Close')


class CompletedRequest(HelpRequest):

    class Meta:
        proxy = True

    object = ManagerHelpRequest()



# @receiver(post_save, sender=Donation)
# def func(sender, instance, **kwargs):
#     c = sender.objects.filter(stock_id=instance.stock_id, state="available")
#     Stocks.objects.select_for_update().filter(id=instance.stock_id).update(occupied_places=c.aggregate(Sum('amount'))['amount__sum'])