from django.contrib import admin

# Register your models here.
from products.models import Category
from .forms import AddcategoryForms
 
# Register your models here.
#to resgister my models in the admin site so i can interact with the table there

class CategoryCreateAdmin(admin.ModelAdmin):
    list_display = ['nom','created_at','updated_at','deleted_at']
    form = AddcategoryForms
    # enables each in admin site based on the category and the item_name
    search_fields= ['nom','created_at']
    # enable filtering by categories
    list_filter = ['nom']
# Register your models here.
admin.site.register(Category,CategoryCreateAdmin)