from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "Cart"

urlpatterns = [
    path("",views.cart_detail, name= "cart_detail"),
    path("add/<int:product_id>", views.cart_add, name = "cart_add"),
    path('remove/<slug:obj_product>/<int:product_id>/', views.cart_remove, name='cart_remove'),
    
]
