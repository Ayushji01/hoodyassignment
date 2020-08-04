from django.db import models

# Create your models here.


class roomdesc(models.Model):
     room_name = models.CharField(max_length=100)
     room_image = models.ImageField(upload_to='pictures', default='SOME STRING')
     room_price = models.IntegerField(default=0)
     room_availability = models.BooleanField(default=False)


    
    
   

