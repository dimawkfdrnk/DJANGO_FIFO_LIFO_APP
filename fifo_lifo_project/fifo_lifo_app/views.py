from django.db import transaction
from django.forms import formset_factory
from django.shortcuts import render, redirect

from .forms import DonationFormNameItem, DonationFormStock, RequestItemFormStock, RequestItemFormNameItem
from .models import DonationItem, HelpRequest, RequestItem, Donation, Stocks


def index(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def session(request):
    request.session['data_session'] = request.POST
    return redirect(request.META['HTTP_REFERER'])


def help_request(request):
    id_stock = None
    amount_items = None
    if request.method == 'POST':
        amount_items = int(request.POST['amount_items'])

    if amount_items:
        if request.session.has_key('data_session'):
            id_stock = request.session['data_session']['stock']
            formset_stock = RequestItemFormStock(initial={'stock': id_stock})
        else:
            formset_stock = RequestItemFormStock()

    elif request.session.has_key('data_session'):
        id_stock = request.session['data_session']['stock']
        formset_stock = RequestItemFormStock(initial={'stock': id_stock})
        amount_items = int(request.session['data_session']['amount_items'])

    RequestItemFormNameItemSet = formset_factory(RequestItemFormNameItem, extra=amount_items)
    formset_name_item = RequestItemFormNameItemSet(prefix='name_item')

    context = {
        "amount_items": amount_items,
        'stocks': Stocks.objects.all(),
        'formset_name_item': formset_name_item,
        'formset_stock': formset_stock,
        'stock': id_stock
    }

    return render(request, 'fifo_lifo_templates/request_item.html', context)


@transaction.atomic()
def request_item(request):
    context = {
        'answer': {}
    }

    RequestItemFormNameItemSet = formset_factory(RequestItemFormNameItem)

    if request.method == "POST":
        stock = RequestItemFormStock(request.POST)
        items = RequestItemFormNameItemSet(request.POST, prefix='name_item')

        if stock.is_valid() and items.is_valid():
            request_object = HelpRequest.objects.create()

            for name_item in items.cleaned_data:
                request_item = RequestItem.objects.create(
                    **stock.cleaned_data,
                    name_item=name_item.get('name_item'),
                    request_id=request_object.id
                )

                donation_item = DonationItem.objects.filter(
                    name_item=request_item.name_item,
                    status='Free',
                    stock_id=request_item.stock_id).last()

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
    disabled_button = False
    id_stock = None
    amount_items = None
    if request.method == 'POST':
        amount_items = int(request.POST['amount_items'])

    if amount_items:
        if request.session.has_key('data_session'):
            id_stock = request.session['data_session']['stock']
            formset_stock = DonationFormStock(initial={'stock': id_stock})
        else:
            formset_stock = DonationFormStock()

    elif request.session.has_key('data_session'):
        id_stock = request.session['data_session']['stock']
        formset_stock = DonationFormStock(initial={'stock': id_stock})
        amount_items = int(request.session['data_session']['amount_items'])


    DonationFormNameItemSet = formset_factory(DonationFormNameItem, extra=amount_items)
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
