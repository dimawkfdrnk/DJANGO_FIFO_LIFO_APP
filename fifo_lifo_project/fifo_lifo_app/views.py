from django.db.models import F
from django.shortcuts import render

from .models import Donation


def index(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def donation(request):
    method = "fifo"
    if method == "fifo":
        donation_item = Donation.objects.order_by('-id')[:1]
    elif method == "lifo":
        donation_item = Donation.objects.order_by('id')[:1]

    for item in donation_item:
        if item.amount > 1:
            Donation.objects.filter(name=item.name).update(amount=item.amount - 1)
        else:
            Donation.objects.filter(name=item.name).delete()

    context = {
        'donation_item': donation_item
    }
    return render(request, 'fifo_lifo_templates/donation_page.html', context)


def donate(request):
    donate_item = Donation.objects.filter(name=request.POST["name"])
    if donate_item:
        Donation.objects.filter(name=request.POST["name"]).update(amount=F('amount') + request.POST["amount"])
    else:
        Donation.objects.create(name=request.POST["name"], amount=request.POST["amount"])

    context = {
        'donate_item': donate_item
    }
    return render(request, 'fifo_lifo_templates/donate_page.html', context)
