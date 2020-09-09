from django.shortcuts import get_object_or_404, render
from .models import Stock, StockInfo
from django.http import HttpResponse


def index(request):
    latest_stock_list = Stock.objects.order_by('-pub_date')[:5]
    context = {
        'latest_stock_list': latest_stock_list,
    }
    return render(request, 'stockcrash/index.html', context)


def detail(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    return render(request, 'stockcrash/detail.html', {'stock': stock})

def results(request, stock_id):
    response = "You're looking at the results of stock %s."
    return HttpResponse(response % stock_id)

def view(request, stock_id):
    return HttpResponse("You're viewing the views of stock %s." % stock_id)