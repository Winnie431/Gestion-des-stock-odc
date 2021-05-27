from django.core import serializers
from django.http import HttpResponse
from category.forms import AddcategoryForms
from django.shortcuts import redirect, render
from products.models import Category

# Create your views here.

#active =Tue sont les produit qui sont pas encore supprimer
def  category_list(request):
    print(request.POST)
    #POUR  recuperer en dure tu fais request;POST['nom'] et apres tu fais form.save
    form = AddcategoryForms(request.POST)

    if (request.method == "POST"):
        # form = AddProductsForms(request.POST)
        if (form.is_valid()):
            form.save()

    category = Category.objects.filter(active = True)
    #create a variable that containds the form created in the form 
    title = 'List of items'  
    context ={
        'category':category,
        'nom':title,
        'form': form
    }
    return render(request, 'category/liste_category.html',context)

def get_category_json(request, id_category):
    # recupere l'id de l'element selectionner
    category = Category.objects.get(id=id_category)
    # look more in use_natural_foreign_keys
    # transforme les donner de la bb en format json
    category_json = serializers.serialize(
        "jsonl", [category], use_natural_foreign_keys=False)
    # return JsonResponse(date = product_json,safe=False)
    # retourne le resultat en format json  comme reponse http
    return HttpResponse(category_json)

def edit_category(request,editID):
    category = Category.objects.get(id = editID) 
    #injecter les information dans le formulaire créer avec la propiréter instance
    form =AddcategoryForms(request.POST, instance= category)
    if (request.method == "POST"):
        # we save the information in the form but not for a new one ,for the product we want to modify so we add instance = product to tell that the product already exitst
        # form = AddProductsForms(request.POST)
        if (form.is_valid()):
            category = form.save(commit=False)
            print(category)
            category.save()
            return redirect("/category/")
        else:
            print("INVALID")

    categorie = Category.objects.filter(active=True)
    # create a variable that containds the form created in the form
    context = {
        'categorie': categorie,
        'nom': 'liste des produits modifier',
        'form': form
    }
    return render(request,'category/liste_category.html', context)