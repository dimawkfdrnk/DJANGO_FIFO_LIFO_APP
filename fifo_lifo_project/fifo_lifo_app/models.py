from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count, F
from django.db import transaction


class Stocks(models.Model):
    name_stock = models.CharField(max_length=100)
    vacancies = models.IntegerField(null=True, default=100)
    occupied_places = models.IntegerField(null=True, default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(vacancies__gte=F('occupied_places')), name="occupied_places_gte")
        ]

    def __str__(self):
        return self.name_stock



class Donation(models.Model):
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE, verbose_name="Выберите склад:")
    name = models.CharField(max_length=30, verbose_name="Что желаете пожертвовать?")
    amount = models.IntegerField(verbose_name="Какое количество?")

    full_name_donator = models.CharField(max_length=50, verbose_name="Ваше ФИО")
    state = models.CharField('Stocks', max_length=20,
                             choices=(
                                 ('available', 'available'),
                                 ('booked', 'booked'),
                                 ('requested', 'requested'),
                                 ('shipped', 'shipped')),
                             default='available'
                             )



@receiver(post_save, sender=Donation)
def func(sender, instance, **kwargs):
    c = sender.objects.filter(stock_id=instance.stock_id, state="available")
    Stocks.objects.select_for_update().filter(id=instance.stock_id).update(occupied_places=c.aggregate(Sum('amount'))['amount__sum'])





