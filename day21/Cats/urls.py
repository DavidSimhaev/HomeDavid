from django.urls import path


from . import views

app_name = "Cats"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    path("breed/", views.allbreed, name="allbreed"),
    path("temps/", views.allTemp, name="allTemp"),
    path("colors/", views.allColor, name="allColor"),
    path("bycolors/<int:color_id>", views.catsbycolor, name="catsbyColor"),
    path("date/", views.allcats, name="allCats"),
    path("temperament/<str:breed_id>", views.statetemperament, name="statetemperament"),
    path("addTemp/", views.add_temp, name="addTemp"),
    path("addBreed/", views.add_breed, name="addBreed"),
    path("addColor/", views.add_color, name="addColor"),
    path("addCat/", views.add_cat, name="addCat"),
]
