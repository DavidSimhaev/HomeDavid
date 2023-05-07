from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "address", "postal_code", "city", "paid", "created", "updated"]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInLine]
    
    def save_model(self, request, obj, form, change):
        for item in self.inlines:
            order_item = item.model
            
        super().save_model(request, obj, form, change)