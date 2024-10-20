from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from job.models import Category

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    city=models.ForeignKey("City", related_name='user_city' ,on_delete=models.CASCADE, null=True, blank=True)
    phone_number=models.CharField(max_length=22)
    image=models.ImageField(upload_to='profil/', height_field=None, width_field=None)
    specialization =models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.user)
        
    

@receiver(post_save ,sender=User)
def update_quantity_on_order_confirmation(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)
        




  
class City(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name