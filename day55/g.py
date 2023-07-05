spisok = ['a', 'b', 'cd', 'are']

for word1 in spisok:
    for word2 in spisok:
        if word1 != word2 and word1.startswith(word2):
            print(word1, word2)