from django.db import models

# Create your models here.
class Stock(models.Model):
    category = models.CharField(max_length = 40, blank = False , null = False)
    item_name = models.CharField(max_length= 40, blank = False , null = False )
    quantity = models.IntegerField(default = 0, blank = False , null =False )
    #celui qui recois le produit
    receive_quantity = models.IntegerField(default = 0, blank = False , null =False )
    receive_by = models.CharField(max_length = 50, blank = False , null = False)
    issue_quantity = models.IntegerField(default = 0, blank = False , null =False )
    #celui qui envoie  le produit
    issue_by = models.CharField(max_length = 50, blank = False , null = False)
    #a qui on a envoyer le produit qui est le même que celui qui recois
    issue_to = models.CharField(max_length = 50, blank = False , null = False)
    reorder_level = models.IntegerField(default = 0, blank = False , null =False )
    last_updated = models.DateTimeField(null= True)

    def __str__(self):
        return self.item_name +' '+ str(self.quantity)