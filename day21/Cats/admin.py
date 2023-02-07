from django.contrib import admin
from .models import Breed, Temperament, Color, Age, Price
# Register your models here.


admin.site.register(Breed)
admin.site.register(Temperament)
admin.site.register(Color)
admin.site.register(Age)
admin.site.register(Price)