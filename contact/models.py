from django.db import models

# Create your models here.
class Info(models.Model):
    contry= models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    street = models.CharField(max_length=50, blank=True, null=True)
    house= models.CharField(max_length=50, blank=True, null=True)
    phone= models.CharField(max_length=20)
    email= models.EmailField(max_length=254)
    worketime=models.CharField(max_length=254)
    class meta:
        pass
    
    def __str__(self):
        return self.email