from django.contrib import admin
from .models import Brand
from .models import Model
from .models import Color
from .models import Recording

# Register your models here.


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Color)
admin.site.register(Recording)
