from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "Main"

urlpatterns = [
    
    path("", views.Main, name="Main"), 
    path("Camers/", views.Camers, name="Camers"),
    path("Lens/", views.Lens, name="Lens"),
    path("Lightings/", views.Lighting, name="Lightings"),
    path("Tripods/", views.Tripods, name="Tripods"),
    path("binoculars/", views.binoculars, name="binoculars"),
    path("Camers/<str:cam_id>/", views.Camera_product, name="Camera_product"),
    path("Lens/<str:lens_id>/", views.Lens_product, name="Lens_product"),
    path("Tripods/<str:trip_id>/", views.Tripods_product, name="Tripods_product"),
    path("Lightings/<str:Lighting_id>/", views.Lighting_product, name="Lighting_product"),

    path("binoculars/<str:Binoculars_id>/", views.Binoculars_product, name="Binoculars_product"),
    
    path(r'^authentication/', views.authentication, name='authentication'),
    path('logout/', views.logout_view, name='logout')
    # Home Page
]
