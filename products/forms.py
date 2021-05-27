from django import forms
from django.forms import widgets
from .models import Products

class AddProductsForms(forms.ModelForm):
    class Meta:
        model = Products
        #enables all field to be present in the add item in the stock pannel 
        #add category to your project
        fields = ['nom','prix','marque',
                    'code','categorie'                   
                     ]
        widgets = {
            'nom':widgets.TextInput(attrs={"class":"form-control"}),
            'prix':widgets.NumberInput(attrs={"class":"form-control"}),
            'marque':widgets.TextInput(attrs={"class":"form-control"}),
            'code':widgets.TextInput(attrs={"class":"form-control"}),
            'categorie':widgets.Select(attrs={"class":"form-control"}),
        }
