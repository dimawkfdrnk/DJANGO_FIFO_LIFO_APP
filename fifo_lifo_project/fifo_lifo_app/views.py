from django.shortcuts import render

from .forms import DonationForm
from .models import Donation


def index(request):
    if request.session.has_key('donate'):
        stock_id = request.session['donate']
        form = DonationForm(initial={'stock': stock_id})
    else:
        form = DonationForm()
    return render(request, 'fifo_lifo_templates/home_page.html', {"form": form})


def donation(request):
    donation_item = Donation.objects.exclude(state="booked")
    method = "lifo"
    if method == "fifo" and donation_item:
        donation_item = donation_item.latest("id")
        Donation.objects.filter(id=donation_item.id).update(state="booked")
    elif method == "lifo" and donation_item:
        donation_item = donation_item.first()
        Donation.objects.filter(id=donation_item.id).update(state="booked")
    return render(request, 'fifo_lifo_templates/donation_page.html', {'donation_item': donation_item})


def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            data_for_session = Donation.objects.create(**form.cleaned_data)
            request.session['donate'] = data_for_session.stock.id
    return render(request, 'fifo_lifo_templates/donate_page.html')
