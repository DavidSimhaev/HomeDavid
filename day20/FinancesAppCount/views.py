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

    # def year(request):
    year = Year.objects.all()
    context = {"Year": year}

    return render(request, "FinancesAppCount/yearincome.html", context)


def yearswithincome(request):
    l = Income.objects.values("year")
    s = []
    for i in l:
        yunit = Year.objects.get(id=i["year"])
        s.append(yunit)
    s = set(s)
    # s = list(s)
    mapper = {"YEARS": s}
    return render(request, "FinancesAppCount/yearincome.html", mapper)


def monthwithincome(request, year_id):
    m = Income.objects.filter(year=year_id)
    months = []
    for income in m:
        months.append(income.month)
    months = set(months)
    # months = list(months)
    # month.sort()
    mapper = {"MONTHS": months, "yearid": year_id}
    return render(request, "FinancesAppCount/monthincome.html", mapper)


def incomepermonth(request, yearid, monthid):
    incomes = Income.objects.filter(year=yearid, month=monthid)
    mapper = {"incomes": incomes}
    return render(request, "FinancesAppCount/sortedincome.html", mapper)
