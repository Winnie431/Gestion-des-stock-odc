from django.urls import path
from .views import fournisseur_view

urlpatterns = [
    path('',fournisseur_view, name = 'fournisseur_view'),
   
    ]