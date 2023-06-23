

def left_join(message_text):
    join_mess = ','.join(message_text)
    replace = join_mess.replace('right', 'left')
    return replace

print(left_join(('lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetuer', 'adipiscing', 'elit', 
                'aenean', 'commodo', 'ligula', 'eget', 'dolor', 'aenean', 'massa', 'cum', 'sociis', 
                'natoque', 'penatibus', 'et', 'magnis', 'dis', 'parturient', 'montes', 'nascetur', 
                'ridiculus', 'mus', 'donec', 'quam', 'felis', 'ultricies', 'nec', 'pellentesque', 
                'eu', 'pretium', 'quis', 'sem', 'nulla', 'consequat', 'massa', 'quis')))
print("The mission is done! Click 'Check Solution' to earn rewards!")
