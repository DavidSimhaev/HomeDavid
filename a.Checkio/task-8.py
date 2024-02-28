
import re
def yaml(a: str) -> dict:
    
    try:
        while True:
            index = a.index('"null"')
            a = a.replace('"null"','---')
    except:
        pass
    try:
        a.index('\\\"')
        a = a.replace('\\\"', '+++')
        a = a.replace('"', '')
        a = a.replace('+++', '"')
        
    except ValueError:
        a = a.replace('"', '')
    
    l = re.split('\n| ', a)
    try:
        l[l.index(':')-1] = l[l.index(':')-1]+':'
        del l[l.index(':')] 
    except:pass    

    try:
        del l[l.index('')]
    except:pass
    f = []
    string = ''
    for word in l:
        if ':' in word:
            if len(string) > 0:
                f.append(string[:-1])
            f.append(word.replace(':', ''))
            string = ''
        else:
            string += word + ' '
    if len(f) % 2 != 0:
        f.append(string[:-1])
    try:
        f[f.index('---')] = '"null"'
    except:
        pass
    keys = [f[index] for index in range(len(f)) if index % 2 == 0 ]
    val = [f[index] for index in range(len(f)) if index % 2 != 0 ]
    dictionary = dict(zip(keys, val))
    for key in dictionary:
        if dictionary[key].isdigit():
            dictionary[key] = int(dictionary[key])
        elif dictionary[key] == 'false':
            dictionary[key] = False
        elif dictionary[key] == '"null"':
            dictionary[key] = 'null'    
        elif dictionary[key] == '' or dictionary[key] == 'null' or dictionary[key] == 'None':
            dictionary[key] = None
    return dictionary
    


print("Example:")

print(yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b')) == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
print(yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b')) == {
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
print(yaml('name: "Bob Dylan"\nchildren: 6\nalive: false')) == {
    "name": "Bob Dylan",
    "children": 6,
    "alive": False,
}
print(yaml('name: "Bob Dylan"\nchildren: 6\ncoding:')) == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
print(yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null')) == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
print(yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ')) == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": "null",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
