from django.contrib import admin
from . models import Topics
from .models import Entry
# Register your models here.


admin.site.register(Topics)
admin.site.register(Entry)