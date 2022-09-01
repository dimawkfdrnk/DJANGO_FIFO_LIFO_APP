from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help_request', views.help_request, name='help_request'),
    path('request_things', views.request_things, name='request_things'),
    path('donation', views.donation, name='donation'),
    path('donation_things', views.donation_things, name='donation_things'),

]
