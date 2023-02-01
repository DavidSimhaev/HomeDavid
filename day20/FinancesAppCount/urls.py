from django.urls import path


from . import views

app_name = "FinancesAppCount"

urlpatterns = [
    #Home Page
    path("", views.index, name= "index"),
    path("incomes/",views.Incomes, name ="incomes"),
    path("yearincome/", views.year, name ="yearincome")
]

