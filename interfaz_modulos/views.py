from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class index_view(TemplateView):
    template_name = 'interfaz/index.html'

