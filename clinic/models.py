from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Doctor(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
        
class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    ci = models.CharField(max_length=50)
    occupation = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=100)
    background = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
    	return self.last_name + ', ' + self.first_name

class Visit(models.Model):
    BACKGROUND_CHOICES = (
        ('first time', 'first time'),
        ('Astenopia', 'Astenopia'),
        ('Glasses broken', 'Glasses broken'),
        ('Uses just G', 'Uses just G'),
        ('Uses just C', 'Uses just C'),
        ('Bifocales', 'Bifocales')
    )
    title = Multiselectfield(choices=BACKGROUND_CHOICES)
    date = models.DateTimeField()
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    
comments = models.CharField(max_length=2000)
