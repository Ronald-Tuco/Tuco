from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Doctor(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
        
class Patient(models.Model):
    first_name = models.CharField("Nombre", max_length=200)
    last_name = models.CharField("Apellido", max_length=200)
    birth_date = models.DateField()
    ci = models.CharField("C.I.", max_length=50)
    occupation = models.CharField("Ocupacion", max_length=200)
    phone = models.CharField("Telefono", max_length=100)
    cellphone = models.CharField("Celular", max_length=100)
    background = models.CharField("Antecedentes", max_length=200)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    gender = models.CharField("Sexo", max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
    	return self.last_name + ', ' + self.first_name

class Visit(models.Model):
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField()
    BACKGROUND_CHOICES = (
        ('first time', 'Primera Vez'),
        ('Glasses broken', 'Rotura de lentes'),
        ('Lost Glasses', 'Extravio de Lentes'),
        ('Uses LC', 'Lentes de Contacto'),
        ('Uses just G', 'Usa solo L'),
        ('Uses just C', 'Usa solo C'),
        ('Bifocales', 'Bifocales'),
        ('RGP', 'RGP'),
        ('Astenopia', 'Astenopia'),
        ('Progresive', 'Progresivas'),
        ('Hidrofilas', 'Hidrofilas')
    )
    title = MultiSelectField("Consulta", choices=BACKGROUND_CHOICES, null=True)  
comments = models.CharField(max_length=2000)
# Create your models here.
