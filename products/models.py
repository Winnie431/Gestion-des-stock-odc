from django.db import models

# Create your models here.
class Products(models.Model):
    nom = models.CharField(max_length = 50, blank = False , null = False, unique = True)
    prix = models.DecimalField(max_digits = 5, decimal_places = 2)
    marque = models.CharField(max_length = 50, blank = False, null = False)
    code = models.CharField(max_length = 10 , unique =True)
    categorie = models.ForeignKey('Category', on_delete = models.DO_NOTHING)  
    active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)    
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.nom

class  Category(models.Model):
    nom = models.CharField(max_length= 50 , blank=False, null = False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.nom
    
    # lhelps relate the foreign key of this table in the table products .search more in this 
    # it return the nom of the categry in the product class other than just the id 
    def natural_key(self):
        return self.nom

class Fournisseur(models.Model):
    nom = models.CharField(max_length= 50 , blank=False, null = False)
    adresse = models.CharField(max_length = 15)

    def __str__(self):
        return self.nom
