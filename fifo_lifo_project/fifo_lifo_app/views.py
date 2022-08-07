from django.shortcuts import render

from .models import Donation

# from .forms import DonationForm

def index(request):
    return render(request, 'fifo_lifo_templates/home_page.html')


def donation(request):
    donation_item = Donation.objects.exclude(state="booked")
    method = "lifo"
    if method == "fifo" and donation_item:
        donation_item = donation_item.latest("id")
        Donation.objects.filter(id=donation_item.id).update(state="booked")
    elif method == "lifo" and donation_item:
        donation_item = donation_item.first()
        Donation.objects.filter(id=donation_item.id).update(state="booked")

    context = {
        'donation_item': donation_item
    }
    return render(request, 'fifo_lifo_templates/donation_page.html', context)


def donate(request):
    Donation.objects.create(
        name=request.POST["name"],
        amount=request.POST["amount"],
        stock_id=9,
        state="available"
    )
    return render(request, 'fifo_lifo_templates/donate_page.html')