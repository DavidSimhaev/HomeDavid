import sys
from Dhelp import DataHelp


def inputImp(question):
    p = input(question)
    if p == ".":
        print("Operation cancelled ")
        sys.exit()
    try:
        n = int(p)
    except:
        print("Please enter number, nothing more!")
        return inputImp(question)
    return n


print("Hello. This is income processing unit")
print("you will be asked for values to enter")
print("For exit just enter .")

datahelp = DataHelp()

while True:
    year = inputImp("Enter year: ")
    month = inputImp("Enter month: ")
    business = inputImp("Enter business: ")
    income = inputImp("Enter income: ")
    # All data saved
    if not datahelp.checkNoExist(year, month, business):
        print("We already have recored for those business and data!")
        y = input("if you want to replace , input y: ")
        if y != "y":
            print("Going to next input")
            next
        else:
            datahelp.replaceData(year, month, business, income)
            print("Record updated")
    else:
        datahelp.insertData(year, month, business, income)
        print("Record inserted")
