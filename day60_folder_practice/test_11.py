try:
    "4"/0
except ArithmeticError:
    print(2)
    
except ZeroDivisionError:
    print(0)

except:
    print(2323)