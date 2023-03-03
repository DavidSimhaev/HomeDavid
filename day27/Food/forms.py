from django import forms

from .models import Restaurant, Menu

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["restaurant", "characteristic", "city", "street", "image"]
        labels = {"restaurant":"Ресторан", "characteristic":"Описание", "city":"Город","street":"Улица", "image":"Лого" }
        
class MenuShefForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["categ","dish","image","price"]
        labels = {"categ":"Добавить категорию","dish":"Блюдо","image":"Фото", "price": "Цена"}
        
        