from django.shortcuts import render, HttpResponse
from django.db.models import F
# from .forms import DonationForm
from .models import RequestThings,HelpRequest,DonationThings,Donation
from django.db import transaction


def index(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def help_request(request):
    if request.method == "POST":
        amount_thing = int(request.POST['amount_thing'])
    return render(request, 'fifo_lifo_templates/help_request.html', {"amount_thing": amount_thing})


@transaction.atomic()
def request_things(request):
    if request.method == "POST":
        data = request.POST
        number_request = HelpRequest.objects.create(full_name=request.POST['full_name_petitioner'])
        print(number_request)
        for number in range(int(data['amount_thing'])):
            RequestThings.objects.create(name_thing=data[f"name{number}"], number_help=number_request)
    return render(request, 'fifo_lifo_templates/home_page.html')


def donation(request):
    if request.method == "POST":
        amount_thing = int(request.POST['amount_thing'])
    return render(request, 'fifo_lifo_templates/donation.html', {"amount_thing": amount_thing})


@transaction.atomic()
def donation_things(request):
    if request.method == "POST":
        data = request.POST
        number_donation = Donation.objects.create(full_name=request.POST['full_name_donator'])
        for number in range(int(data['amount_thing'])):
            DonationThings.objects.create(name_thing=data[f"name{number}"], number_donation=number_donation)
    return render(request, 'fifo_lifo_templates/home_page.html')










