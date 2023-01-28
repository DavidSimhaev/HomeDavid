import flet as fl
from flet import Page, Text, Row, IconButton, Column, slider


def main(page: Page):
    page.title = "Test Window"
    page.vertical_alignment = "center"
    n = 0

    def add_click(e):
        digits = int(label.value) + 1
        label.value = str(digits)
        page.update()

    def remove_click(e):
        digits = int(label.value) - 1
        label.value = str(digits)
        page.update()

    def slider_change(e):
        slibel.value = slider.value
        page.update()

    label = Text(value="0", color=fl.colors.RED, size=40)
    slibel = Text(value=0, color=fl.colors.BLACK, size=40)
    slider = fl.Slider(min=0, max=100, divisions=10, value=0, on_change=slider_change)
    button_add = IconButton(
        fl.icons.ADD, on_click=add_click, icon_size=40, icon_color=fl.colors.GREEN
    )
    button_remove = IconButton(
        fl.icons.REMOVE, on_click=remove_click, icon_size=40, icon_color=fl.colors.RED
    )

    page.add(
        Column([slibel, slider, label, button_add, button_remove], alignment="center")
    )


fl.app(target=main)
