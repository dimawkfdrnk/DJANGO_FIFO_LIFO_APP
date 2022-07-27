from django.shortcuts import render

from fifo_lifo import Stock

stock_1 = Stock("fifo")

def index(request):
    return render(request, 'fifo_lifo_templates/home_page.html')

def donation(request):
    return render(request, 'fifo_lifo_templates/donation_page.html', {'stock': stock_1.gift()})

def donate(request):
    name = request.POST["name"]
    amount = request.POST["amount"]
    stock_1.donation(name, int(amount))
    return render(request, 'fifo_lifo_templates/donate_page.html')