from django.shortcuts import render
from django.db.models import F
from .forms import DonationForm
from .models import Donation, Stocks
from django.db import transaction


def index(request):
    if request.session.has_key('donate'):
        session_data = request.session['donate']
        form = DonationForm(initial={
            'stock': session_data['stock_id'],
            'full_name_donator': session_data['full_name'],
        })
    else:
        form = DonationForm()

    return render(request, 'fifo_lifo_templates/home_page.html', {"form": form})


def donation(request):
    donation_item = Donation.objects.select_for_update().exclude(state="booked")
    method = "lifo"
    if method == "fifo" and donation_item:
        donation_item = donation_item.latest("id")
        donation_item.state = "booked"
        donation_item.save()

    elif method == "lifo" and donation_item:
        donation_item = donation_item.first()
        donation_item.state = "booked"
        donation_item.save()
    return render(request, 'fifo_lifo_templates/donation_page.html', {'donation_item': donation_item})

@transaction.atomic()
def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            data_for_session = Donation.objects.create(**form.cleaned_data)
            print(data_for_session)
            request.session['donate'] = {
                "stock_id": data_for_session.stock.id,
                "full_name": data_for_session.full_name_donator
            }


    return render(request, 'fifo_lifo_templates/donate_page.html')


