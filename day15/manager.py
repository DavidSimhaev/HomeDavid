from Dhelp import DataHelp
import matplotlib.pyplot as plt
import sys

def inputImp(question):
    print('1 income grouped by business for all period')
    p = input(question)
    if p == '.':
        print('Operation cancelled ')
        sys.exit()
        
        
    
    try:
        n = int(p)
    except:
        print('Please enter number, nothing more!')
        return (inputImp(question))
    return n

print('Welcome to manager command center')
print('please choose your option')
print('For exit just enter .')




dataHelp = DataHelp()
while True:
    print('1)income grouped by business for all period, \n2)income  grouped by years for all period\n3)maximum income of a month in a year')
    choice = input('Enter your choice: ')
    if choice == '1':
        query = 'SELECT business, sum(income) from predicator.train group by business order by business;'
        l = dataHelp.executeQuery(query)
        print(l)
        pass
    if choice == "2":
        query = "SELECT sum(income), year from predicator.train group by year order by year"
        l = dataHelp.executeQuery(query)
        print(l)
        pass
    if choice == "3":
        query = "SELECT max(income), year from predicator.train group by year order by year;"
        l = dataHelp.executeQuery(query)
        print(l)
        pass
    
    
    
    
    y = list(map(lambda x: x[0], l))
    x = list(map(lambda x: x[1], l))
    fig, axs = plt.subplots(1,1)
    axs.bar(x, height= y)
    axs.set_xlabel("Год", fontsize = 14)
    axs.set_ylabel("Доход", fontsize = 14)
    plt.show()
        

        
        