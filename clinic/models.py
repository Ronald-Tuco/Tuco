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
    doctor = models.ForeignKey(Doctor, verbose_name="Doctor")
    patient = models.ForeignKey(Patient, verbose_name="Paciente")
    date = models.DateTimeField("Fecha")
    BACKGROUND_CHOICES = (
        ('first_time', 'Primera Vez'),
        ('broken_lasses', 'Rotura de lentes'),
        ('lost_glasses', 'Extravio de Lentes'),
        ('uses_lc', 'Lentes de Contacto'),
        ('uses_jf', 'Usa solo L'),
        ('uses_jn', 'Usa solo C'),
        ('bifocales', 'Bifocales'),
        ('rgp', 'RGP'),
        ('astenopia', 'Astenopia'),
        ('progresive', 'Progresivas'),
        ('hidrofilas', 'Hidrofilas')
    )
    title = MultiSelectField("Consulta", choices=BACKGROUND_CHOICES, null=True)  
    mc = models.CharField("Motivo de la Consulta", max_length=2000, null=True)
    app = models.CharField("APP", max_length=2000, null=True)
    apf = models.CharField("APF", max_length=2000, null=True)
    od = models.CharField("OD", max_length=50, null=True)
    ol = models.CharField("OL", max_length=50, null=True)
    convergencia = models.CharField("Convergencia", max_length=50, null=True)
    eyere = models.CharField("Reflejos pupilares", max_length=100, null=True)
comments = models.CharField(max_length=2000)
# Create your models here.
