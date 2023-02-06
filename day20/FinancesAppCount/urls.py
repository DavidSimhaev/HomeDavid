from django.urls import path


from . import views

app_name = "FinancesAppCount"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    path("incomes/", views.Incomes, name="incomes"),
    path("yearincome/", views.yearswithincome, name="ylist"),
    path("months/<int:year_id>", views.monthwithincome, name="mlist"),
    path(
        "sortedincomes/<int:yearid>/<int:monthid>", views.incomepermonth, name="ilist"
    ),
]
