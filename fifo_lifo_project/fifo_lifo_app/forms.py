from django import forms

from .models import DonationItem, Stocks, RequestItem


class DonationFormStock(forms.ModelForm):
    
    class Meta:
        model = DonationItem
        fields = ['stock']

        widgets = {
            "stock": forms.Select(attrs={"class": "form-control", "onChange": "form.submit();"} )
        }


class DonationFormNameItem(forms.ModelForm):

    class Meta:
        model = DonationItem
        fields = ['name_item']

        widgets = {
            "name_item": forms.TextInput(attrs={"class": "form-control"}),
        }


class RequestItemFormStock(forms.ModelForm):
    class Meta:
        model = RequestItem
        fields = ['stock']

        widgets = {
            "stock": forms.Select(attrs={"class": "form-control", "onChange": "form.submit();"})
        }

class RequestItemFormNameItem(forms.ModelForm):

    class Meta:
        model = RequestItem
        fields = ['name_item']

        widgets = {
            "name_item": forms.TextInput(attrs={"class": "form-control"}),
        }