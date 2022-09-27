from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help_request', views.help_request, name='help_request'),
    path('request_item', views.request_item, name='request_item'),
    path('end_registration', views.end_registration, name='end_registration'),
    path('donation', views.donation, name='donation'),
    path('donation_item', views.donation_item, name='donation_item'),
    path('sesstion', views.session, name='session'),
    path('search_for_item', views.search_for_item, name='search_for_item'),
    path('searching_results', views.searching_results, name='searching_results')

]
