from django.contrib import admin
from .models import BMW
from .models import AUDI
from .models import Zhiguli

# Register your models here.

admin.site.register(BMW)
admin.site.register(AUDI)
admin.site.register(Zhiguli)
