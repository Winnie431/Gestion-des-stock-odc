from django.urls import path
from .views import home_view,list_items

urlpatterns = [
    path('',home_view, name = 'stock_home'),
    # path('stock/',list_items,name = 'list_items'),
    ]