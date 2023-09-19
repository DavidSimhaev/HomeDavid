from django.contrib import admin
from .models import Category,Camera, lens, tripods, Categorys_lighting, lightings, Binoculars
# Register your models here.
admin.site.register(Category)

admin.site.register(Camera)

admin.site.register(lens)

admin.site.register(tripods)

admin.site.register(lightings)

admin.site.register(Categorys_lighting)

admin.site.register(Binoculars)