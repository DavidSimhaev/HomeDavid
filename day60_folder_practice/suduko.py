






from pprint import pprint


def Suduko(suduko):
    res = []
    l_suduko = []
    index = 0
    for number in suduko:
        index+=1
        l_suduko.append(number)
        if index == 9:
            index = 0
            res.append(l_suduko)
            l_suduko = []
    end = None
    c = 0
    for index in range(len(res)):
        if end:
            c = 0
        for number in res[index]:
            try:
                check1 = [number == res[x][index+c] for x in range(9)]
            except:
                pass
            check2 = [number == res[index][x] for x in range(9)]
            print("---------------------------------")
            print(check1)
            print(check2)
            print("---------------------------------")
            if str(check1).count("True") > 1 and str(check2).count("True") > 1 :
                return False
            c+=1
            end = True
    return True
suduko = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"

pprint(Suduko(suduko))

            
[['2', '9', '5', '7', '4', '3', '8', '6', '1'],
 ['4', '3', '1', '8', '6', '5', '9', '2', '7'],
 ['8', '7', '6', '1', '9', '2', '5', '4', '3'],
 ['3', '8', '7', '4', '5', '9', '2', '1', '6'],
 ['6', '1', '2', '3', '8', '7', '4', '9', '5'],
 ['5', '4', '9', '2', '1', '6', '7', '3', '8'],
 ['7', '6', '3', '5', '2', '4', '1', '8', '9'],
 ['9', '2', '8', '6', '7', '1', '3', '5', '4'],
 ['1', '5', '4', '9', '3', '8', '6', '7', '2']]


suduko = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"

pprint(Suduko(suduko))
