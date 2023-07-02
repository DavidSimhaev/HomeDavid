def checkio(text: str) -> str:
    l = [text.count(text[index]) for index in range(len(text)) if text[index] != "!" and text[index] != " " and text[index] not in "1234567890" ] # показывает сколько повторений
    alfabet = list(map(chr, range(97, 123))) # Английский алфавит в слусаи если все символы не повторяются
    
    
    check_if_all_one = all(map(lambda x: x==1, l)) # Символы не повторяются
    Bigs_letter = list(filter(lambda x: x.isupper(), text))
    if Bigs_letter == []:
        if check_if_all_one:
            for letter in alfabet:
                for index in range(len(text)):
                    if text[index] == letter:
                        return text[index]
    try:
        for index in range(len(Bigs_letter)):
            if Bigs_letter[index] == Bigs_letter[index+1]:
                return Bigs_letter[index].lower()
    except:
        text = text.replace(" ", "")
        text = text.replace("!", "")
        if check_if_all_one:
            for letter in alfabet:
                for index in range(len(text)):
                    if text[index] == letter:
                        return text[index]
        else:
            
            for index in range(len(text)):
                if text[index] == text[l.index(max(l))]:
                    return text[index]






# These "print(s" are used for self-checking
print( checkio("Hello World!")) == "l"
print( checkio("How do you do?")) == "o"
print( checkio("One")) == "e"
print( checkio("Oops!")) == "o"
print( checkio("AAaooo!!!!")) == "a"
print( checkio("abe")) == "a"
print(checkio('fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;lzcdkcslksdkseewme,'))
print(checkio('Lorem ipsum dolor sit amet'))
print("The mission is done! Click 'Check Solution' to earn rewards!")