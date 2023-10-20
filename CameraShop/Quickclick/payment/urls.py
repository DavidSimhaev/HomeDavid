from django.urls import path
from . import views
from . import webhooks
app_name = 'payment'

urlpatterns=[
    path('process/', views.payment_process, name='process'),
    path('completed/<str:order_id>', views.payment_completed, name='completed'),
    path('cancaled/', views.payment_canceled, name='canceled'),
    path('webhook/',webhooks.stripe_webhook , name='stripe_webhook'),
]