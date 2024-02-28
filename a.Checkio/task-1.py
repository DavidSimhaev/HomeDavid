def count_digits(text: str) -> int:
    l = []
    for i in text:
        try:
            int(i)
            l.append(i)
        except ValueError:
            continue
    return len(l)


print("Example:")
print(count_digits("hi"))

# These "asserts" are used for self-checking
print(count_digits("hi") == 0)
print(count_digits("who is 1st here") == 1)
print(count_digits("my numbers is 2") == 1)
print((
    count_digits(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 8
))
print(count_digits("5 plus 6 is") == 2)
print(count_digits("") == 0)

print("The mission is done! Click 'Check Solution' to earn rewards!")

def safe_pawns(pawns) -> int:
    
    places = 'abcdefgh'
    l = []
    for position in pawns:
        lineY = position[1]
        if int(lineY) >= 8:
            continue
        lineX = position[0]
        if lineX == 'a':
           if 'b'+str(int(lineY)+1) in pawns and 'g'+str(int(lineY)+1) not in l:
               l.append('b'+str(int(lineY)+1))
               
               
        elif lineX == 'h':
           if 'g'+str(int(lineY)+1) in pawns and 'g'+str(int(lineY)+1) not in l:
               l.append('g'+str(int(lineY)+1))
        else:
            try:
                next_poziton_LEFT = str(places[places.find(lineX) - 1]) + str(int(lineY)+1) # позиция слева
                next_poziton_RIGTH = str(places[places.find(lineX) + 1]) + str(int(lineY)+1)  
                if next_poziton_LEFT in pawns and next_poziton_LEFT not in l:
                    l.append(next_poziton_LEFT)
                    
                if next_poziton_RIGTH in pawns and next_poziton_RIGTH not in l :
                    l.append(next_poziton_RIGTH)
                    
            except:
                pass
    return len(set(l))
                   



print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

print(safe_pawns({"f4", "d4", "e3", "b4", "g5", "d2", "c3"}))# == 6
print(safe_pawns({"f4", "c4", "b4", "e4", "g4", "d4", "e5"}))# == 1)
print(safe_pawns({'a1', 'd4', 'c3', 'f6', 'h8', 'b2', 'e5', 'g7'}))# == 7
print(safe_pawns({'f6', 'd4', 'h8', 'g7', 'b2', 'c3', 'e5', 'a1'}))# 
print(safe_pawns(('g3', 'f2', 'h2', 'b6', 'g1', 'a7', 'c7', 'b8')))# == 6 

print("The mission is done! Click 'Check Solution' to earn rewards!")
