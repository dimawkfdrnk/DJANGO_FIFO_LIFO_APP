from  django import forms
from django.db.models import F
from .models import Donation, Stocks

class DonationForm(forms.ModelForm):
    class Meta:

        model = Donation
        fields = ["stock", "name", "amount", "full_name_donator"]
        widgets = {
            "stock": forms.Select(attrs={"class": "form-control"}),
            "full_name_donator": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"})
        }




