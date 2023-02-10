from django import forms

from .models import Price

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ["breed","temperament","color", "age", "price"]
        labels = {"breed": "Порода", "temperament": "Характер", "color": "Окрас", "age": "Возраст", "price": "ЦЕНА"}
