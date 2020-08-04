from django.db import models

# Create your models here.
class bookroom(models.Model):
    room_number = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField(default='2020-01-01')
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    
    