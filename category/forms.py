from django import forms
from django.forms import widgets
from products.models import Category

class AddcategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        #enables all field to be present in the add item in the stock pannel 
        #add category to your project
        fields = ['nom',]
        widgets = {
            'nom':widgets.TextInput(attrs={"class":"form-control"}),
            # 'updated_at':widgets.DateTimeInput(attrs={"class":"form-control"}),
            

        }