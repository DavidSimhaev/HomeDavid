from django.shortcuts import render
from .models import Year
from .models import Income
# Create your views here.

def index(request):
    """Home page of application"""
    return render(request, "FinancesAppCount/index.html")

def Incomes(request):
    incomes = Income.objects.order_by("date_added")
    content = {"incomes": incomes}
    return render(request, "FinancesAppCount/incomes.html", content)

def year(request):
    year = Year.objects.all()
    context = {"Year": year}
    return render(request, "FinancesAppCount/income.html", context)