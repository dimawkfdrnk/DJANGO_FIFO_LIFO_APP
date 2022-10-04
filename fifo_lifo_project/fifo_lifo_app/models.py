from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

SELECT_A_PRODUCT_CATEGORY = [("Верхняя одежда", "Верхняя одежда"),
                             ("Нижнее бельё", "Нижнее бельё"),
                             ("Еда", "Еда")]


class Stocks(models.Model):
    name_stock = models.CharField(max_length=30, verbose_name="Склад")
    vacancies = models.IntegerField(null=True, default=10, verbose_name="Количество мест")
    occupied_places = models.IntegerField(null=True, default=0, verbose_name="Занятые места")

    class Meta:
        verbose_name = 'cклад'
        verbose_name_plural = 'Склады'
        constraints = [
            models.CheckConstraint(check=models.Q(vacancies__gte=F('occupied_places')), name='occupied_places_gte')
        ]

    def __str__(self):
        return self.name_stock


class ItemDescription(models.Model):
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE, null=True, verbose_name="Склад")
    name_item = models.CharField(max_length=50, verbose_name="Название вещи")
    category = models.CharField(max_length=20, choices=SELECT_A_PRODUCT_CATEGORY,verbose_name="Категория")
    # size = models.CharField(max_length=20, choices=SELECT_A_PRODUCT_CATEGORY,verbose_name="Размер")
    # gender = models.CharField(max_length=20, choices=SELECT_A_PRODUCT_CATEGORY,verbose_name="Пол")

    class Meta:
        abstract = True


class HelpRequest(models.Model):
    status = models.CharField(
        max_length=15,
        choices=(("Open", "Open"), ("Close", "Close")),
        default="Open",
        verbose_name="Статус"
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'запрос помощи'
        verbose_name_plural = 'Запросы помощи'


class RequestItem(ItemDescription):
    request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE, null=True, verbose_name="Номер прошения")
    status = models.CharField(
        max_length=15,
        choices=(("Open", "Open"), ("Close", "Close")),
        default="Open",
        verbose_name="Статус"
    )
    class Meta:
        verbose_name = 'запрошеная вещь'
        verbose_name_plural = 'Запрошенные вещи'


class Donation(models.Model):

    class Meta:
        verbose_name = 'пожертвование'
        verbose_name_plural = 'Пожертвования'

    # def __str__(self):
    #     return self.id


class DonationItem(ItemDescription):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True, verbose_name="Номер пожертвования")
    status = models.CharField(
        max_length=15,
        choices=(("Free", "Free"), ("Issued", "Issued")),
        default="Free",
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = 'вещь которую пожертвовали'
        verbose_name_plural = 'Вещи которые пожертвовали'

    def __str__(self):
        return self.name_item


class ManagerHelpRequest(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="Close")


class CompletedRequest(HelpRequest):
    class Meta:
        proxy = True
        verbose_name = 'завершенный запрос'
        verbose_name_plural = 'Завершенные запросы'

    object = ManagerHelpRequest()


@receiver(post_save, sender=DonationItem)
def func(sender, instance, **kwargs):
    occupied_places_count = sender.objects.filter(stock_id=instance.stock_id, status="Free").count()
    Stocks.objects.select_for_update().filter(id=instance.stock_id).update(occupied_places=occupied_places_count)
