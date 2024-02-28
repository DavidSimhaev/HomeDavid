from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "Main"

urlpatterns = [
    
    path("", views.Main, name="Main"), 
    path("Camers/", views.Camers, name="Camers"),
    path(r"^C_filtred/", views.Camers_filtred, name="Camers_filtred"),
    path("Filtred_Camers/", views.Camers_filtred, name="Camers_Filtred"),
    path("Lens/", views.Lens, name="Lens"),
    path(r"^L_filtred/", views.Lens_filtred, name="Lens_filtred"),
    path("Lightings/", views.Lighting, name="Lightings"),
    path("Tripods/", views.Tripods, name="Tripods"),
    path("binoculars/", views.binoculars, name="binoculars"),
    path("Camers/<str:cam_id>/<slug:obj_product>/", views.Camera_product, name="Camers_product"),
    path("Lens/<str:lens_id>/<slug:obj_product>/", views.Lens_product, name="Lens_product"),
    path("Tripods/<str:trip_id>/<slug:obj_product>/", views.Tripods_product, name="Tripods_product"),
    path("Lightings/<str:Lighting_id>/<slug:obj_product>/", views.Lighting_product, name="Lightings_product"),
    path("binoculars/<str:Binoculars_id>/<slug:obj_product>/", views.Binoculars_product, name="binoculars_product"),
    path("Profile/", views.Profile_Page, name = "Profile"),
    path(r'^authentication/', views.authentication, name='authentication'),
    path("Change_process/", views.Change_Profile_Name, name = "Change_Name"),
    path("Change_process-2/", views.Change_Profile_Last, name = "Change_Last"),
    path("Change_process-3/", views.Change_Profile_Email, name = "Change_Email"),
    path("Change_process-4/", views.Change_Profile_Foto, name = "Change_Foto"),
    path("ErrorNoGetData", views.ErrorGetData, name="ErrorGetData"),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path(r'^SearchAll/', views.SearchAll, name='SearchAll'),
    
    path('logout/', views.logout_view, name='logout'),
    
    # Home Page
]
#url(r'^result/(?P<result>[^\/]*)/$', views.result, name='result'),