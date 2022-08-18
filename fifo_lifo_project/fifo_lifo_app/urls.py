from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donation', views.donation, name='donation'),
    path('donate', views.donate, name='donate'),

]
