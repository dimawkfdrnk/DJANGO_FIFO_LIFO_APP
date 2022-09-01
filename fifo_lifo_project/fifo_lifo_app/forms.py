from  django import forms
from django.db.models import F
from .models import Donation, Stocks



# class DonationForm(forms.ModelForm):
#
#     stock = forms.ModelChoiceField(queryset=Stocks.objects.exclude(occupied_places__gte=F("vacancies")),
#                                    label="Выберите склад",
#                                    widget=forms.Select(attrs={"class": "form-control"}))
#     class Meta:
#
#         model = Donation
#         fields = ["name", "amount", "full_name_donator"]
#         widgets = {
#             "full_name_donator": forms.TextInput(attrs={"class": "form-control"}),
#             "name": forms.TextInput(attrs={"class": "form-control"}),
#             "amount": forms.NumberInput(attrs={"class": "form-control"})
#         }
from  django import forms
from django.forms import ModelForm
from .models import Donation, Stocks



class DonationForm(forms.Form):
    # stock = forms.ModelChoiceField(
    #     queryset=Stocks.objects.all(),
    #     label= "Пункт приема",
    #     widget=forms.Select(attrs={"class": "form-control"})
    # )
    name = forms.CharField(
        max_length=30,
        label= "Что жертвуете?",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    amount = forms.IntegerField(
        label= "Сколько?",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )



