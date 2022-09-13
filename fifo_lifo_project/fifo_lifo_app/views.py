from django.db import transaction
from django.shortcuts import render

from .models import DonationItem, HelpRequest, RequestItem, Donation, Stocks


def index(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def help_request(request):
    if request.method == "POST":
        amount_items = int(request.POST['amount_items'])
    context = {
        "amount_items": amount_items,
        'stocks': Stocks.objects.all()
    }

    return render(request, 'fifo_lifo_templates/request_item.html', context)


@transaction.atomic()
def request_item(request):

    context = {
        'answer': {}
    }

    if request.method == "POST":
        data = request.POST
        request_object = HelpRequest.objects.create()

        for number in range(int(data['amount_items'])):
            request_item = RequestItem.objects.create(
                name_item=data[f"name{number}"],
                request_id=request_object.id,
                stock_id=request.POST['id_stock'])
            donation_item = DonationItem.objects.filter(
                name_item=request_item.name_item,
                status='Free',
                stock_id=request.POST['id_stock']).last()

            if donation_item:
                request_item.status = 'Close'
                donation_item.status = 'Issued'
                request_item.save()
                donation_item.save()
                context['answer'][request_item.name_item] = donation_item

        help_request_check = RequestItem.objects.filter(request_id=request_object.id, status='Open')
        if not help_request_check:
            request_object.status = 'Close'
            request_object.save()

    return render(request, 'fifo_lifo_templates/end_registration.html', context)


def end_registration(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def donation(request):
    if request.method == "POST":
        amount_items = int(request.POST['amount_items'])
        id_stock = None
        disabled_button  = False
        if 'id_stock' in request.POST:
            id_stock = request.POST['id_stock']
        stock = Stocks.objects.filter(id=id_stock)
        for i in stock:
            if i.occupied_places >= i.vacancies:
                disabled_button = True

    context = {
        "amount_items": amount_items,
        'stocks': Stocks.objects.all(),
        'id_stock': id_stock,
        'disabled_button': disabled_button
    }

    return render(request, 'fifo_lifo_templates/donation_item.html', context)


@transaction.atomic()
def donation_item(request):
    if request.method == "POST":
        data = request.POST
        # print(data)
        donation_object = Donation.objects.create()

        for number in range(int(data['amount_items'])):
            DonationItem.objects.create(
                name_item=data[f"name{number}"],
                donation_id=donation_object.id,
                stock_id=request.POST['id_stock']
            )

    return render(request, 'fifo_lifo_templates/home_page.html')
