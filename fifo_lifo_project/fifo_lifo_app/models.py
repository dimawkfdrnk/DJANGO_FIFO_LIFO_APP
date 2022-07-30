from django.db import models


# class Stock(models.Model):
#     address = models.CharField(db_column='Адрес', max_length=100)


class Donation(models.Model):
    # stocks = models.ForeignKey(Stock, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.IntegerField()



# class Donate(models.Model):
#     donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
#     amount = models.IntegerField(db_column='Количество')
#     issuing_time = models.DateTimeField(db_column='Дата выдачи')
#     full_name_recipients = models.CharField(db_column='ФИО', max_length=50)
