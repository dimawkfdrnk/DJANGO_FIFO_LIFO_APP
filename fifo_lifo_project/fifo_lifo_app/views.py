from django.shortcuts import render, HttpResponse
from django.db.models import F
# from .forms import DonationForm
from .models import DonationItem,HelpRequest,RequestItem,Donation
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
        request_id = HelpRequest.objects.create(full_name_petitioner=request.POST['full_name_petitioner'])
        for number in range(int(data['amount_thing'])):
            RequestItem.objects.create(name_item=data[f"name{number}"], request_id=request_id)
    return render(request, 'fifo_lifo_templates/home_page.html')


def donation(request):
    if request.method == "POST":
        amount_thing = int(request.POST['amount_thing'])
    return render(request, 'fifo_lifo_templates/donation.html', {"amount_thing": amount_thing})


@transaction.atomic()
def donation_things(request):
    if request.method == "POST":
        data = request.POST
        donation_id = Donation.objects.create(full_name_donator=request.POST['full_name_donator'])
        for number in range(int(data['amount_thing'])):
            DonationItem.objects.create(name_item=data[f"name{number}"], donation_id=donation_id)
    return render(request, 'fifo_lifo_templates/home_page.html')







# def index(request):
#     if request.session.has_key('donate'):
#         session_data = request.session['donate']
#         form = DonationForm(initial={
#             'stock': session_data['stock_id'],
#             'full_name_donator': session_data['full_name'],
#         })
#     else:
#         form = DonationForm()
#
#     return render(request, 'fifo_lifo_templates/home_page.html', {"form": form})
#
# @transaction.atomic()
# def donation(request):
#     donation_item = Donation.objects.select_for_update().exclude(state="booked")
#     method = "lifo"
#     if method == "fifo" and donation_item:
#         donation_item = donation_item.latest("id")
#         donation_item.state = "booked"
#         donation_item.save()
#
#     elif method == "lifo" and donation_item:
#         donation_item = donation_item.first()
#         donation_item.state = "booked"
#         donation_item.save()
#     return render(request, 'fifo_lifo_templates/help_request.html', {'donation_item': donation_item})
#
# @transaction.atomic()
# def donate(request):
#     if request.method == "POST":
#         form = DonationForm(request.POST)
#         if form.is_valid():
#             data_for_session = Donation.objects.create(**form.cleaned_data)
#             request.session['donate'] = {
#                 "stock_id": data_for_session.stock.id,
#                 "full_name": data_for_session.full_name_donator
#             }
#
#     return render(request, 'fifo_lifo_templates/donation.html')


