from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Modelo de perfil.
# Este modelo nos permite almacenar las claves de acceso a la API de Twiiter ademas del ID del usuario principal.

class perfiles(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    id_twitter = models.CharField(max_length=256, default='')
    consumer_key = models.CharField(max_length=256, default='')
    consumer_secret = models.CharField(max_length=256, default='')
    access_token = models.CharField(max_length=256, default='')
    access_token_secret = models.CharField(max_length=256, default='')

    # Este metodo nos sirve para mostrar en el Panel de Administracion los mensajes.
    def __str__(self):
        # Estas variables son para añadirle seguridad a las claves de la API.
        key = ''
        key_secret = ''
        token = ''
        token_secret = ''

        # Analizamos el consumer_key para ver si esta completa.
        if self.consumer_key == '':
            key = 'Vacio'
        else:
            key = 'Completo'

        # Analizamos el consumer_secret para ver si esta completa.
        if self.consumer_secret == '':
            key_secret = 'Vacio'
        else:
            key_secret = 'Completo'

        # Analizamos el access_token para ver si esta completa.
        if self.access_token == '':
            token = 'Vacio'
        else:
            token = 'Completo'

        # Analizamos el access_token_secret para ver si esta completa.
        if self.access_token_secret == '':
            token_secret = 'Vacio'
        else:
            token_secret = 'Completo'

        return "Usuario: " + str(self.usuario) + ", id_twitter: " + str(self.id_twitter) + \
               ", consumer_key: " + str(key) + ", consumer_secret: " + str(key_secret) + \
               ", access_token: " + str(token) + ", access_token_secret: " + str(token_secret) + "."

# Con estas anotaciones obligamos que al introducir una tupla en la tabla User, tambien se cree un perfil.
@receiver(post_save, sender=User)
def crear_usuario_crear_perfil(sender, instance, created, **kwargs):
    if created:
        perfiles.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_guardar_perfil(sender, instance, **kwargs):
    instance.perfiles.save()


class Alarmcontrol(models.Model):
    fecha = models.CharField(max_length=50, default='')
    texto = models.CharField(max_length=256, default='')
    usuario = models.CharField(max_length=256, default='')