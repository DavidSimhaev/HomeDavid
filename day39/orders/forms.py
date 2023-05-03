from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]
        labels = {"first_name": "Имя", "last_name": "Фамилия", "email": "Мейл", "address": "Адрес", "postal_code": "Индекс", "city":"Город" }