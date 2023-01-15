

# Первый способ через цикл фор. Посчитать сколько всего прибыли
year2018 = []
summa2018 = []
year2019 = []
summa2019 = []
year2020 = []
summa2020 = []
year2021 = []
summa2021 = []
year2022 = []
summa2022 = []


#2018
for i in new_list["2018"]:
    year2018.append(i)
for y in year2018:
    summa2018.append(y[2])
for i in new_list.keys():
    if i == "2018":
        summa2018 = sum(summa2018)
        print("Cумма за 2018 год:")
        print(summa2018)
print("---------------------------------------------------------------------------")
#2019
for i in new_list["2019"]:
    year2019.append(i)
for y in year2019:
    summa2019.append(y[2])
for i in new_list.keys():
    if i == "2019":
        summa2019 = sum(summa2019)
        print("Cумма за 2019 год:")
        print(summa2019)
print("---------------------------------------------------------------------------")
#2020
for i in new_list["2020"]:
    year2020.append(i)
for y in year2020:
    summa2020.append(y[2])
for i in new_list.keys():
    if i == "2020":
        summa2020 = sum(summa2020)
        print("Cумма за 2020 год:")
        print(summa2020)
print("---------------------------------------------------------------------------")
#2021
for i in new_list["2021"]:
    year2021.append(i)
for y in year2021:
    summa2021.append(y[2])
for i in new_list.keys():
    if i == "2021":
        summa2021 = sum(summa2021)
        print("Cумма за 2021 год:")
        print(summa2021)
print("---------------------------------------------------------------------------")
#2022
for i in new_list["2022"]:
    year2022.append(i)
for y in year2022:
    summa2022.append(y[2])
for i in new_list.keys():
    if i == "2022":
        summa2022 = sum(summa2022)
        print("Cумма за 2022 год:")
        print(summa2022)

yearswork = [summa2018,summa2019,summa2020,summa2021,summa2022] # Весь доход за 4 года
print(f"Весь доход за 4 года: {sum(yearswork)}") # 39761225603.46

print("____________________________________________________________________________________________")




