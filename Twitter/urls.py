"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Twitter.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, name='logout'),
    path('lgn/', customlogin, name='lgn'),
    path('lgo/', customlogout, name='lgo'),
    path('cg/', cargar, name='cargar'),
    path('principal/', principal, name='principal'),
    path('comprobar/', comprobar, name='comprobar'),
    path('comprobaram/', comprobaramistad, name='comprobaram'),
    path('cargartweets/', cargargeotweets, name='cargartweets'),
    path('pprueba/', Filtrartweet, name='pprueba'),
    path('seguimiento/', Seguimientoalarma, name='alarma'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)