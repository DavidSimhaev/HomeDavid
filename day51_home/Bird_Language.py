# Птичка меняет слова по следующим правилам:
#- после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
#- после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);


 
 
def translate(phrase):
    VOWELS = "aeiouy"
    i = 0
    new_phrase = ''
    while i < len(phrase):
        if phrase[i] == ' ':
            new_phrase += phrase[i]
            i += 1
        elif phrase[i] in VOWELS:
            new_phrase += phrase[i]
            i += 3
        else:
            new_phrase += phrase[i]
            i += 2
    return new_phrase
 

                                    

                  


print("Example:")
print(translate("hieeelalaooo")) == "hello"
print(translate("hoooowe yyyooouuu duoooiiine")) == "how you doin"
print(translate("aaa bo cy da eee fe")) == "a b c d e f"

# These "asserts" are used for self-checking


print(translate("sooooso aaaaaaaaa"))# == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")