from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "Main"

urlpatterns = [
    
    path("", views.Main, name="Main"), 
    path("FunDay/", views.FunDay, name="FunDay"), 
    path("FunDay/Confirmation/", views.WriteDateCustemer, name="WriteDateCustemer"), 
    path("FunDay/PaymentProcces/", views.PaymentProcces, name="PaymentProcces"), 
    path("FunDay/Payment_Completed/", views.payment_completed, name="payment_completed"), 
    path("FunDay/Payment_Canceled/", views.payment_canceled, name="payment_canceled"), 
    
    
]
