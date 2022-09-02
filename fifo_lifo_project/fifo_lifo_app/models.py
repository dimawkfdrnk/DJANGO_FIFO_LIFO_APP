from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count, F
from django.db import transaction

class AbstractModel_1(models.Model):
    full_name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class AbstractModel_2(models.Model):
    name_thing = models.CharField(max_length=40)

    class Meta:
        abstract = True


class HelpRequest(AbstractModel_1):
    pass



class RequestThings(AbstractModel_2):
    number_help = models.ForeignKey(HelpRequest, on_delete=models.CASCADE, null=True)



class Donation(AbstractModel_1):
    pass



class DonationThings(AbstractModel_2):
    number_donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True)













