from django.contrib import admin
from .models import Android
from .models import Apple
from .models import Xiaomi
# Register your models here.

admin.site.register(Android)
admin.site.register(Apple)
admin.site.register(Xiaomi)