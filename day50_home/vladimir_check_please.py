FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "zero",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"
def checkio(num: int) -> str:
    for str_number in range(len(FIRST_TEN)+1):
        if num == str_number:
            return FIRST_TEN[str_number-1]
    for str_number in range(len(SECOND_TEN)):
        if num == str_number + 10:
            return SECOND_TEN[str_number]
    if num >= 20 and num < 100:
        for str_number in range(20, 100):
            if int(str(num)[1]) == 0 and num == str_number:
                return OTHER_TENS[int(str(str_number)[0])]
            elif num == str_number:
                return OTHER_TENS[int(str(str_number)[0])] +" "+ FIRST_TEN[int(str(str_number)[1])-1]  
    if num >= 100: 
        for str_number in range(100,1000):
            if int(str(num)[1]) == 0 and int(str(num)[2]) == 0 and num == str_number:
                return FIRST_TEN[int(str(str_number)[0])-1] + " " + HUNDRED
            elif int(str(num)[0]) == int(str(str_number)[0]) and int(str(num)[1]) == 0 and int(str(num)[2]) == int(str(str_number)[2]): # Выходит если в середине ноль
                return FIRST_TEN[int(str(str_number)[0])-1] + " " + HUNDRED + " " + FIRST_TEN[int(str(str_number)[2])-1]            
            elif int(str(num)[0]) == int(str(str_number)[0]) and int(str(num)[1]) == int(str(str_number)[1]) and int(str(num)[2]) == int(str(str_number)[2]):
                if int(str(num)[1]) == 1:
                    return FIRST_TEN[int(str(str_number)[0])-1] + " " + HUNDRED + " " + SECOND_TEN[int(str(str_number)[1])+int(str(str_number)[2])-1]
                elif int(str(num)[2]) == 0: 
                    return FIRST_TEN[int(str(str_number)[0])-1] + " " + HUNDRED + " " + OTHER_TENS[int(str(str_number)[1])]
                else:
                    return FIRST_TEN[int(str(str_number)[0])-1] + " " + HUNDRED + " " + OTHER_TENS[int(str(str_number)[1])] + " " + FIRST_TEN[int(str(str_number)[2])-1]
    return ""
print("Example:")
#print(checkio(4))

print(checkio(200))
print("The mission is done! Click 'Check Solution' to earn rewards!")
