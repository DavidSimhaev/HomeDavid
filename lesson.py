import plotly.express as px
from flet.plotly_chart import PlotlyChart
import flet as ft
import plotly.graph_objects as go
from flet import Page
import pandas
import solver


def main(page: Page):
    xdata = range(1, 11)
    ydata = list(map(lambda t: solver.solve(f"sin{t},+5*cos(2*{t})"), xdata))

    # style = px.data.gapminder().query("continent=='Oceania'")
    # fig = px.line(style, x="year", y="lifeExp", color = "country")
    df = pandas.DataFrame(dict(x=xdata, y=ydata))

    fig = px.line(df, x="x", y="y", title="Squares")

    page.add(Text("Test"), PlotlyChart(fig, expand=False))


ft.app(target=main)
