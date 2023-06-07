def correct_sentence(text: str) -> str:
    
    l = []
    for index in range(len(text)):
        if index == 0:
            l.append(text[0].upper())
        else:
            l.extend(text[1::])
            if l[-1] != ".":
                l.extend(".")
            ready = "".join(l)
            return ready


print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
print(correct_sentence("greetings, friends"))# == "Greetings, friends."
print(correct_sentence("Greetings, friends"))# == "Greetings, friends."
print(correct_sentence("Greetings, friends."))# == "Greetings, friends."
print(correct_sentence("greetings, friends."))# == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")
