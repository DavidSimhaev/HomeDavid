import flet as ft
from flet import Page, IconButton, Text, TextField
from Dhelp import DataHelp

datahelp = DataHelp()



def main(page: Page):
    
    page.window_width = 1000 
    page.bgcolor = "#E5B8F4"
    
    def submit1(e):
        try:
            year = int(yearText.value)
            monthText.focus()
        except:
            dlg.open = True
            page.dialog = dlg
            yearText.focus()
            page.update()
            
        
    def submit2(e):
        try:
            month = int(monthText.value)
            businessText.focus()
        except:
            dlg.open = True
            page.dialog = dlg
            monthText.focus()
            page.update()
            
            
            
    def submit3(e):
        try:
            business = int(businessText.value)
            IncomeText.focus()
        except:
            dlg.open = True
            page.dialog = dlg
            businessText.focus()
            page.update()
            
    
    def close_dlg(e):
        dlg.open = False
        page.update()
    
    def close_dlg2(e):
        dlg2.open = False
        page.update()
    
    def close_dlg3(e):
        dlg3.open = False
        page.update()
    
    
    def close_and_change(e):
        datahelp.replaceData(yearText.value, monthText.value, businessText.value, IncomeText.value)
        dlg2.open = False
        print("Record updated")
        page.update()
        
    
    
    
    def add_click(e):
        while True:
            if not datahelp.checkNoExist(yearText.value, monthText.value, businessText.value):
                dlg2.open = True
                page.dialog = dlg2
            else:
                datahelp.insertData(yearText.value, monthText.value, businessText.value, IncomeText.value)
                dlg3.open = True
                page.dialog = dlg3
                
            page.update()
            return
        
    
    dlg = ft.AlertDialog(modal= True, title=ft.Text("Data error!"), content= ft.Text("Please check if data is integer"), actions= [ft.TextButton("Ok", on_click=close_dlg)] )
    
    dlg2 = ft.AlertDialog(modal= True, title=ft.Text("We already have recored for those business and data!"), content= ft.Text("if you want to replace?"), actions= [ft.TextButton("Yes", on_click=close_and_change), ft.TextButton("No, Thank", on_click= close_dlg2)] )
    
    dlg3 = ft.AlertDialog(modal= True, title=ft.Text("Record inserted!"), actions= [ft.TextButton("Ok", on_click=close_dlg3)] )
    
    
    
    
    yearLabel = Text("Year: ", color= ft.colors.BLACK, size = 40)
    yearText  = TextField(value="", color= ft.colors.BLUE, text_size = 40, on_submit=submit1)
    yearRow = ft.Row([yearLabel, yearText], alignment= "center", )

    monthLabel = Text("Month: ", color= ft.colors.BLACK, size = 40)
    monthText  = TextField(value="", color= ft.colors.BLUE, text_size = 40, on_submit= submit2)
    monthRow = ft.Row([monthLabel, monthText], alignment= "center")
    
    
    businessLabel = Text("Business: ", color= ft.colors.BLACK, size = 40)
    businessText  = TextField(value="", color= ft.colors.BLUE, text_size = 40, on_submit= submit3)
    businessRow = ft.Row([businessLabel, businessText], alignment= "center")
    
    IncomeLabel = Text("Income: ", color= ft.colors.BLACK, size = 40)
    IncomeText  = TextField(value="", color= ft.colors.BLUE, text_size = 40, on_submit=add_click)
    IncomeRow = ft.Row([IncomeLabel, IncomeText], alignment= "center")
    
    addBtn = ft.ElevatedButton(text="add",color=ft.colors.BLACK, on_click=add_click)
    
    
    page.add(ft.Column([yearRow, monthRow, businessRow, IncomeRow,addBtn]))
    
    


ft.app(target=main)