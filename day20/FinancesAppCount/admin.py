from django.contrib import admin
from .models import Year
from .models import Month
from .models import Business
from .models import Income
# Register your models here.


admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Business)
admin.site.register(Income)
