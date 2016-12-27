from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    ci = models.CharField(max_length=50)
    occupation = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=100)
    background = models.CharField(max_length=200)
    
    def __str__(self):
    	return self.last_name + ', ' + self.first_name

# Create your models here.
