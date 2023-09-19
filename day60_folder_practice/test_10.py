

def read_int(prompt, _min, _max):
    #
    # Write your code here.
    #
    
    try:
        int(prompt)
          # - 10
        if int(prompt) > _min and int(prompt) < _max:
            return int(prompt)
        else:
            print("Error: the value is not within permitted range (-10..10)")
    except ValueError:
        print("Error: please enter number, not str and not float")
    


v = read_int(input("Enter a number from -10 to 10: "), -10, 10)
if v != None:
    print("The number is:", v)



