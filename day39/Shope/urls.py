from django.urls import path


from . import views

app_name = "Shope"

urlpatterns = [
    # Home Page
    path("product/", views.product_list, name="product_list"),
]
