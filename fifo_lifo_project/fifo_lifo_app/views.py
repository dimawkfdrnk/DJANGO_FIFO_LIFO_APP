from django.db import transaction
from django.shortcuts import render
from  .forms import DonationFormNameItem, DonationFormStock
from .models import DonationItem, HelpRequest, RequestItem, Donation, Stocks
from django.forms import formset_factory



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
            context['answer'][request_item.name_item] = donation_item

            if donation_item:
                request_item.status = 'Close'
                donation_item.status = 'Issued'
                request_item.save()
                donation_item.save()

        help_request_check = RequestItem.objects.filter(request_id=request_object.id, status='Open')
        if not help_request_check:
            request_object.status = 'Close'
            request_object.save()

    return render(request, 'fifo_lifo_templates/end_registration.html', context)


def end_registration(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def donation(request):
    disabled_button = False
    id_stock = None

    if 'stock' in request.POST:
        id_stock = request.POST['stock']
        formset_stock = DonationFormStock(initial={'stock': id_stock})
    else:
        formset_stock = DonationFormStock()

    if request.method == "POST":
        amount_items = int(request.POST['amount_items'])
    DonationFormNameItemSet = formset_factory(DonationFormNameItem, extra=2, max_num=amount_items)
    formset_name_item = DonationFormNameItemSet(prefix='name_item')

    stock = Stocks.objects.filter(id=id_stock)
    for i in stock:
        if i.occupied_places >= i.vacancies:
            disabled_button = True

    context = {
        "amount_items": amount_items,
        'formset_stock': formset_stock,
        'formset_name_item': formset_name_item,
        'disabled_button': disabled_button,
        'stock': id_stock
    }

    return render(request, 'fifo_lifo_templates/donation_item.html', context)


@transaction.atomic()
def donation_item(request):
    DonationFormNameItemSet = formset_factory(DonationFormNameItem)

    if request.method == "POST":
        stock = DonationFormStock(request.POST)
        items = DonationFormNameItemSet(request.POST, prefix='name_item')

        if stock.is_valid() and items.is_valid():
            donation = Donation.objects.create()

            for name_item in items.cleaned_data:
                DonationItem.objects.create(
                    **stock.cleaned_data,
                    name_item=name_item.get('name_item'),
                    donation_id=donation.id)

    return render(request, 'fifo_lifo_templates/home_page.html')

