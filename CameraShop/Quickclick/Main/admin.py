from django.contrib import admin
from .models import Color, Category,Camera, lens, tripods, Categorys_lighting, lightings, Binoculars, IMG_FILES, IMG_FILES_LENS, IMG_FILES_TRIPODS, IMG_FILES_LIGHTS, IMG_FILES_BINOCULARS, account_data
# Register your models here.

admin.site.register(Color)


admin.site.register(Category)

admin.site.register(Camera)

admin.site.register(lens)

admin.site.register(tripods)

admin.site.register(lightings)

admin.site.register(Categorys_lighting)

admin.site.register(Binoculars)

admin.site.register(IMG_FILES)

admin.site.register(IMG_FILES_LENS)

admin.site.register(IMG_FILES_TRIPODS)

admin.site.register(IMG_FILES_LIGHTS)

admin.site.register(IMG_FILES_BINOCULARS)


admin.site.register(account_data)