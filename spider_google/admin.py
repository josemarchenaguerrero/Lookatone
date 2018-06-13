from django.contrib import admin
from spider_google.models import paises, idiomas, spider_html, spider_html_incidencia

# Register your models here.
admin.site.register(paises)
admin.site.register(idiomas)
admin.site.register(spider_html)
admin.site.register(spider_html_incidencia)