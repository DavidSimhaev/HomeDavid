import plotly.express as px
from flet.plotly_chart import PlotlyChart
import flet as ft
import pandas
import plotly.graph_objects as go
from flet import Page, Text
import solver

def main(page: Page):
    xdata = list(range(-2000,2001))
    ydata = list(map(lambda t: solver.solve(f"sin({t})+{t}*cos(({t})*2)") , xdata))
    #style = px.data.gapminder().query("continent=='Oceania'")
    #fig = px.line(style, x= "year", y= "lifeExp", color = "country")
    #fig = go.Figure(data = [go.layout.shape.Line()])
    
    df = pandas.DataFrame(dict(
        x = xdata,
        y = ydata
    ))
    fig = px.line(df, x="x", y="y", title= "Squares")

    page.add(Text("Test"), PlotlyChart(fig, expand= False))
    
ft.app(target=main)