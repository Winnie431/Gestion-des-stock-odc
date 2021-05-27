from django.urls import path
from .views import  get_product_json, products_list,show_product,edit_product

urlpatterns = [
    # path('',home_view, name = 'home_view'),
    path('',products_list, name ='products_list'),
    path('products/<int:id_produit>',show_product, name ='show_product'),
    path('api/products/<int:id_product>',get_product_json, name ='product_json'),
    path('editproduct/<int:editID>',edit_product, name='edit_product')
    ]