from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help_request', views.help_request, name='help_request'),
    path('request_item', views.request_item, name='request_item'),
    path('end_registration', views.end_registration, name='end_registration'),
    path('donation', views.donation, name='donation'),
    path('donation_item', views.donation_item, name='donation_item')
    ,

]
