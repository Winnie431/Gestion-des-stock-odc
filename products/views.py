from django.http.response import JsonResponse
from products.forms import AddProductsForms
from products.models import Products
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


def products_list(request):
    print(request.POST)
    # POUR  recuperer en dure tu fais request;POST['nom'] et apres tu fais form.save
    form = AddProductsForms(request.POST)

    if (request.method == "POST"):
        # form = AddProductsForms(request.POST)
        if (form.is_valid()):
            form.save()

    produits = Products.objects.filter(active=True)
    # create a variable that containds the form created in the form
    context = {
        'produits': produits,
        'nom': 'liste des produits',
        'form': form
    }
    return render(request, 'products/acceuil.html', context)


def get_product_json(request, id_product):
    # recupere l'id de l'element selectionner
    product = Products.objects.get(id=id_product)
    # look more in use_natural_foreign_keys
    # transforme les donner de la bb en format json
    product_json = serializers.serialize(
        "jsonl", [product], use_natural_foreign_keys=True)
    # return JsonResponse(date = product_json,safe=False)
    # retourne le resultat en format json  comme reponse http
    return HttpResponse(product_json)

def edit_product(request,editID):
    product = Products.objects.get(id = editID) 
    #injecter les information dans le formulaire créer avec la propiréter instance
    form =AddProductsForms(request.POST, instance= product)
    if (request.method == "POST"):
        # we save the information in the form but not for a new one ,for the product we want to modify so we add instance = product to tell that the product already exitst
        # form = AddProductsForms(request.POST)
        if (form.is_valid()):
            product = form.save(commit=False)
            print(product)
            product.save()
        else:
            print("INVALID")

    produits = Products.objects.filter(active=True)
    # create a variable that containds the form created in the form
    context = {
        'produits': produits,
        'nom': 'liste des produits modifier',
        'form': form
    }
    return render(request, 'products/acceuil.html', context)


def show_product(request, **kwargs):
    # produit = Products.objects.get(id = kwargs.get('id_produit'))
    # try:
    #    produit = Products.objects.get(id = kwargs.get('id_produit'))
    # except Products.DoesNotExist:
    #     # reponse ='<h1>not found</h1>'
    #     raise Http404('the product is not available')
    # produit = get_object_or_404(Products,id=kwargs.get('id_produit'))
    return HttpResponse()
