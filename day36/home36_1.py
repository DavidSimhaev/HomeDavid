

def show_letters(some_str):
    clean_str = ''.join(letter for letter in some_str if letter.isalpha())
    for symbol in clean_str:
        if symbol == "плохое слово":
            print("Не ругайтесь")
            yield symbol


show_letters("плохое слово")