from django.shortcuts import render, HttpResponse
# from django.db.models import F
# from .forms import DonationForm
from .models import DonationItem, HelpRequest, RequestItem, Donation, CompletedRequest
from django.db import transaction


def index(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def help_request(request):
    if request.method == "POST":
        amount_items = int(request.POST['amount_items'])
    return render(request, 'fifo_lifo_templates/request_item.html', {"amount_items": amount_items})


@transaction.atomic()
def request_item(request):
    if request.method == "POST":
        data = request.POST
        request_object = HelpRequest.objects.create(full_name_petitioner=request.POST['full_name_petitioner'])
        for number in range(int(data['amount_items'])):
            request_item = RequestItem.objects.create(name_item=data[f"name{number}"], request_id=request_object.id)
            donation_item = DonationItem.objects.filter(name_item=request_item.name_item).last()
            if donation_item:
                request_item.status = 'Close'
                request_item.save()
                donation_item.status = 'Issued'
                donation_item.save()
        help_request_check = RequestItem.objects.filter(request_id=request_object.id, status='Open')
        if not help_request_check:
            request_object.status = 'Close'
            request_object.save()

    context = {
        's': donation_item
    }
    return render(request, 'fifo_lifo_templates/home_page.html', context)


def donation(request):
    if request.method == "POST":
        amount_items = int(request.POST['amount_items'])
    return render(request, 'fifo_lifo_templates/donation_item.html', {"amount_items": amount_items})


@transaction.atomic()
def donation_item(request):
    if request.method == "POST":
        data = request.POST
        donation_object = Donation.objects.create(full_name_donator=request.POST['full_name_donator'])
        for number in range(int(data['amount_items'])):
            DonationItem.objects.create(name_item=data[f"name{number}"], donation_id=donation_object.id)
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
#     return render(request, 'fifo_lifo_templates/request_item.html', {'donation_item': donation_item})
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
#     return render(request, 'fifo_lifo_templates/donation_item.html')


