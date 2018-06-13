from django import forms

class Crearpelicula(forms.Form):
    img1 = forms.ImageField(required=True,label='')
    img2 = forms.ImageField(required=True, label='')
    img3 = forms.ImageField(required=True, label='')
    img4 = forms.ImageField(required=True, label='')
    img5 = forms.ImageField(required=True, label='')
    img6 = forms.ImageField(required=True, label='')
    img7 = forms.ImageField(required=True, label='')
    img8= forms.ImageField(required=True, label='')
    img9 = forms.ImageField(required=True, label='')
    img10 = forms.ImageField(required=True, label='')


    def clean(self):
        clean_data = self.cleaned_data
        return clean_data