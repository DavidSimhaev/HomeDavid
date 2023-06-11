# Птичка меняет слова по следующим правилам:
#- после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
#- после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);

def translate(text: str) -> str:
    l = []
    for index in range(len(text)):
        if text[index] not in "aeiouy" :
            l.extend(text[index])

        else:
            try:
                if text[index-1] not in "aeiouy" and text[index-1] != " ":
                    continue
            
                elif text[index] == text[index+1] and text[index] == text[index+2] and text[index] != text[index+3]:
                    l.extend(text[index])
                
                elif text[index] == text[index+1] and text[index] == text[index+2] and text[index+3] in "aeiouy":
                    if text.count(text[index])+1 > 3:
                        number = text.count(text[index])/3
                        l.extend(text[index]*int(number))
                        break
            except:
                l.extend(text[index+1])  
    res = "".join(l)
    return res

                                    

                  


print("Example:")
print(translate("hieeelalaooo")) == "hello"
print(translate("hoooowe yyyooouuu duoooiiine")) == "how you doin"
print(translate("aaa bo cy da eee fe")) == "a b c d e f"

# These "asserts" are used for self-checking


print(translate("sooooso aaaaaaaaa"))# == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")