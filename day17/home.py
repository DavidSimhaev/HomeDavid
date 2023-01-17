import plotly.express as px
import matplotlib.pyplot as plt
import flet as ft
from flet.plotly_chart import PlotlyChart
from itertools import groupby
from superclassapi import GetFromApi

url = "https://datausa.io/api"
method = "data"
parameters = {'drilldowns': 'State', 'measures': 'Population', 'year': '2018'}

l = GetFromApi(url).addMethod(method=method, parameters=parameters).GetDataFromApi().GetValueFromKey("data")



state =[]
for x in l:
    state.append(x["State"])

poplation =[]
for y in l:
    poplation.append(y["Population"])

fig, axs = plt.subplots(1,1)
axs.bar(state, height= poplation)
axs.set_xlabel("Штат", fontsize = 14,)
axs.set_ylabel("Популяция", fontsize = 14)
plt.xticks(state, rotation=90)
plt.show()


