from django.contrib import admin

# Register your models here.
from .models import OrderItem, Order, Food, Massage, ORDER_ID 
# Register your models here.


admin.site.register(Order)

admin.site.register(Food)

admin.site.register(Massage)

admin.site.register(OrderItem)

admin.site.register(ORDER_ID)


