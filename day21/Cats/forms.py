from django import forms

from .models import Temperament, Breed, Price

class TempForm(forms.ModelForm):
    class Meta:
        model = Temperament
        fields = ['temperament']
        labels = {'temperament': ''}
        
class BreedForm(forms.ModelForm):
    class Meta:
        model = Price # Я застрял
        fields = ['breed']
        labels = {'breed': ''}