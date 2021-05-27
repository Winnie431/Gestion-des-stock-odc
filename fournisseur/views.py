from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fournisseur_view(request, *args , **kwargs):
    return  render(request, 'fournisseur/liste_fournisseur.html')