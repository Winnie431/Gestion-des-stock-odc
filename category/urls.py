from django.urls import path
from category.views import category_list, edit_category, get_category_json

urlpatterns = [
    path('',category_list, name = 'category_list'),
    path('api/category/<int:id_category>',get_category_json, name ='category_json'),
    path('editcategory/<int:editID>',edit_category, name='edit_category')
    
    ]
