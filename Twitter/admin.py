from django.contrib import admin
from Twitter.models import perfiles

# Administracion del modulo Perfiles.

class PerfilesAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_filter = ('usuario', 'id_twitter')
    search_fields = ['usuario']
    ordening = ('usuario', 'id_twitter')


# Register your models here.

admin.site.register(perfiles, PerfilesAdmin)