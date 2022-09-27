from django import forms

from .models import DonationItem, Stocks, RequestItem


class FormStock(forms.ModelForm):
    
    class Meta:
        model = DonationItem
        fields = ['stock']

        widgets = {
            'stock': forms.Select(attrs={'class': 'form-control', 'onChange': 'form.submit();'} )
        }


class DonationFormNameItem(forms.ModelForm):

    class Meta:
        model = DonationItem
        fields = ['category', 'name_item']

        widgets = {
            'name_item': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # "size": forms.Select(attrs={"class": "form-control"}),
            # "gender": forms.Select(attrs={"class": "form-control"})
        }


class RequestItemFormNameItem(forms.ModelForm):

    class Meta:
        model = RequestItem
        fields = ['name_item']

        widgets = {
            'name_item': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SearchItemForm(forms.ModelForm):

    class Meta:
        model = DonationItem
        fields = ['name_item', 'category']

        widgets = {
            'name_item': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'search'}),
            'category': forms.Select(attrs={'class': 'form-control'})}