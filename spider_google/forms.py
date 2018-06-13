from django import forms
from spider_google.models import idiomas, paises

class buscador_googleForm(forms.Form):
    barra_buscador = forms.CharField(max_length=1000)
    bus_and = forms.CharField(max_length=1000, required=False)
    bus_or = forms.CharField(max_length=1000, widget=forms.Textarea, required=False)
    bus_exclusion = forms.CharField(max_length=1000, widget=forms.Textarea, required=False)
    bus_dominio = forms.CharField(max_length=4000, widget=forms.Textarea, required=False)
    bus_dominio_relacionado = forms.CharField(max_length=4000, widget=forms.Textarea, required=False)
    bus_dominio_enlazado = forms.CharField(max_length=4000, widget=forms.Textarea, required=False)
    bus_filtro_avanzado = forms.CharField(max_length=4000, widget=forms.Textarea, required=False)
    bus_extension_archivo = forms.CharField(max_length=4000, widget=forms.Textarea, required=False)
    bus_fecha = forms.CharField(max_length=2, required=False)
    bus_profundidad = forms.IntegerField(min_value=0, max_value=5, required=False)
    bus_num = forms.IntegerField(min_value=0, max_value=100, required=False)

    bus_pais = forms.ChoiceField(
        choices=paises.objects.all().order_by('nombre').values_list('reduccion', 'nombre'),
        widget=forms.RadioSelect,
        required=False,
    )

    bus_idioma = forms.ChoiceField(
        choices=idiomas.objects.all().order_by('nombre').values_list('reduccion', 'nombre'),
        widget=forms.RadioSelect,
        required=False,
    )