import plotly.express as px
import flet as ft
from flet.plotly_chart import PlotlyChart
from superclassapi import GetFromApi
from itertools import groupby
url = "https://datausa.io/api"
method = "data"
parameters = {'drilldowns': 'State', 'measures': 'Population'}

l = GetFromApi(url).addMethod(method=method, parameters=parameters).GetDataFromApi().GetValueFromKey("data")
print(l)

w = list(map(lambda t: (t[0], list(map(lambda g: (g["State"],g["Population"]),t[1]))),groupby(l, lambda x: x["Year"])))
w= dict(reversed(w))

print(w)

x= "".join(i[0]+"," for i in w["2013"]).split(",")

y= [i[1] for i in w["2013"]]
print("-----------------")
print(x, y)
del x[-1]
def main(page: ft.Page):
    
    fig = px.bar(
        w,
        x= "".join(i[0]+"," for i in w["2013"]).split(","),
        y=[i[1] for i in w["2013"]],
        height=400,
    )

    page.add(PlotlyChart(fig, expand=True))
 
ft.app(target=main)