from stock_mgmt.models import Stock
from django.shortcuts import render


# Create your views here.

def home_view(request , *args, **kwargs):
    return render(request , 'stock/home.html') 

def list_items(request, *args, **kwargs):
    title = 'List of items'
    queryset= Stock.objects.all()
    context = {
        'title':title,
        'queryset':queryset,
    }
    return render (request ,'list_items/list_items.html', context)

    # def add_items(request, *args, **kwargs):
    # title = 'List of items'
    # queryset= Stock.objects.all()
    # context = {
    #     'title':title,
    #     'queryset':queryset,
    # }
    # return render (request ,'list_items/list_items.html', context)