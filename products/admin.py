from django.contrib import admin
from .models import Products
from .forms import AddProductsForms
 
# Register your models here.
#to resgister my models in the admin site so i can interact with the table there

class ProductsCreateAdmin(admin.ModelAdmin):
    list_display = ['nom','prix','marque','code','categorie','created_at']
    form = AddProductsForms
    # enables each in admin site based on the category and the item_name
    search_fields= ['nom','prix']
    # enable filtering by categories
    list_filter = ['nom']
# Register your models here.
admin.site.register(Products,ProductsCreateAdmin)