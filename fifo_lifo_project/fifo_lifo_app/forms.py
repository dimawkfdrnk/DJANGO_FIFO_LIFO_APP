from django import forms
from django.forms import formset_factory

from .models import DonationItem, Stocks


class DonationForm(forms.ModelForm):
    stock = forms.ModelChoiceField(queryset=Stocks.objects.all(),
                                   label="Выберите склад",
                                   widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = DonationItem
        fields = ['name_item']

        widgets = {
            "name_item": forms.TextInput(attrs={"class": "form-control"}),
        }

    def formset_func(self, max_num=None):
        return formset_factory(DonationForm, extra=2, max_num=max_num)
