from  django import forms
from django.db.models import F
from .models import DonationItem, Stocks
from django.forms import formset_factory


class DonationForm(forms.ModelForm):

    stock = forms.ModelChoiceField(queryset=Stocks.objects.all(),
                                   label="Выберите склад",
                                   widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:

        model = DonationItem
        fields = ['name_item']

        widgets = {
            "name_item": forms.TextInput(attrs={"class": "form-control" }),
        }


DonationFormSet = formset_factory(DonationForm, extra=20)
