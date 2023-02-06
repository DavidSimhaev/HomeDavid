from django.urls import path


from . import views

app_name = "Phone"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    path("date/", views.allPhones, name="date"),
    path("brand/", views.allBrand, name="brand"),
    path("model/<str:brand_id>", views.choicemodel, name="Choisemodel"),
    path("spicmodel/", views.model, name="model")
    
    
    
    
]