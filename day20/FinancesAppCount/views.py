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
    context = {"Year":year}
    
    return render(request, "FinancesAppCount/yearincome.html", context)




#def year(request, year_id):
    year = Year.objects.get(year=year_id)
    idY = year.id
    incomes = Income.objects.filter(year=idY)
    entries = incomes.order_by('income')
    context = {"Year":year,"yearincome": entries}
    return render(request, "FinancesAppCount/yearincome.html", context) # Здесь возращаем запрос, 