import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class paises(models.Model):
    america_norte = 'America Norte'
    america_ser = 'America Sur'
    america_central = 'America Central'
    antartida = 'Antartida'
    asia = 'Asia'
    europa = 'Europa'
    oceania = 'Oceania'
    africa = 'Africa'

    continentes_choices = (
        (america_norte, 'America Norte'),
        (america_ser, 'America Sur'),
        (america_central, 'America Central'),
        (asia, 'Asia'),
        (europa, 'Europa'),
        (oceania, 'Oceania'),
        (africa, 'Africa'),
        (antartida, 'Antartida'),
    )

    nombre = models.CharField(max_length=100)
    reduccion = models.CharField(max_length=2)
    continente = models.CharField(max_length=50, choices=continentes_choices)

    def __str__(self):
        return "Nombre: " + str(self.nombre) +", reduccion: " + str(self.reduccion) + ", continente: " + str(self.continente)

class idiomas(models.Model):
    nombre = models.CharField(max_length=100)
    reduccion = models.CharField(max_length=5)

    def __str__(self):
        return "Nombre: " + str(self.nombre) + ", reduccion: " + str(self.reduccion)


class spider_html(models.Model):
    filtro = models.CharField(max_length=200)
    subfiltro = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    fecha = models.CharField(max_length=10, editable=False)
    hora = models.CharField(max_length=5, editable=False)
    html = models.FileField(upload_to='HTML/', blank=True)

    def save(self, *args, **kwargs):
        self.fecha = datetime.datetime.now().strftime('%d-%m-%Y')
        self.hora = datetime.datetime.now().strftime('%H:%M')
        return super(spider_html, self).save(*args, **kwargs)

    def __str__(self):
        return "Id: " + str(self.id) + ", filtro: " + str(self.filtro) + ", subfiltro: " + str(self.subfiltro) + ", titulo: " + str(self.titulo) +\
               ", url: " + str(self.url) + ", fecha: " + str(self.fecha) + ", hora: " + str(self.hora) + \
               ", html: " + str(self.html)

class spider_html_incidencia(models.Model):
    spider_html = models.ForeignKey(spider_html, on_delete=models.CASCADE)
    incidencia = models.TextField()

    def __str__(self):
        return "Id: " + str(self.id) + ", spider_html: " + str(self.spider_html) + ", incidencia: " + str(self.incidencia)
