

def left_join(phrases: tuple[str]) -> str:
    l = []
    if_its_not_right = []
    for index_word in range(len(phrases)):
        word_right = "right"
        word_right = list(word_right)
        for index_letter in range(len(phrases[index_word])):
            if len(phrases[index_word]) == 1:
                    l.append(phrases[index_word]+",")
                    continue 
            for letter_check in word_right:
                if letter_check == phrases[index_word][index_letter]: # Если последующий символ из серии right
                    word_right.remove(word_right[0]) # Убираем элемент что проверить следующий ход
                    if_its_not_right.extend(phrases[index_word][index_letter])
                    check_letter = True
                    break
                check_letter = False
                break
            def check(word,if_not_right):
                if len(word) == 0:
                    if_its_not_right.clear()
                    return False
                if if_not_right:
                    return True
                else:
                    return False 
            if check(word_right, check_letter) == True: # Если мы продолжаем бежать по циклу и делать проверку
                if phrases[index_word][-1] == "r":
                    l.extend(phrases[index_word][index_letter]+",")
                    word_right = "right"
                    word_right = list(word_right)
                    if_its_not_right.clear()
                    break
                continue
            if check_letter:             
                try:
                    phrases[index_word][index_letter+1] # Когда есть следующий элемент запяту ставить не нужно
                    l.extend("left")
                    word_right = "right"
                    word_right = list(word_right) 
                    if_its_not_right.clear()
                except:
                    l.extend("left,") # Когда все нормально и следующего элемента нет 
                    word_right = "right"
                    word_right = list(word_right)
                    if_its_not_right.clear()
            else:
                if if_its_not_right:
                    l.extend(if_its_not_right)
                    l.extend(phrases[index_word][index_letter])
                    if_its_not_right.clear()
                else:
                    l.extend(phrases[index_word][index_letter])
                try:
                    phrases[index_word][index_letter+1]
                except:
                    l.extend(",")
    res = "".join(l)
    return res[:-1]    
print("Example:")
#print(left_join(("left", "right", "left", "stop")))

# These "asserts" are used for self-checking

print(left_join(('lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetuer', 'adipiscing', 'elit', 
                'aenean', 'commodo', 'ligula', 'eget', 'dolor', 'aenean', 'massa', 'cum', 'sociis', 
                'natoque', 'penatibus', 'et', 'magnis', 'dis', 'parturient', 'montes', 'nascetur', 
                'ridiculus', 'mus', 'donec', 'quam', 'felis', 'ultricies', 'nec', 'pellentesque', 
                'eu', 'pretium', 'quis', 'sem', 'nulla', 'consequat', 'massa', 'quis')))
print("The mission is done! Click 'Check Solution' to earn rewards!")





