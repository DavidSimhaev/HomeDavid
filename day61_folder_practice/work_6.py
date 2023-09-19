
def create_file(file):
    file = open(f"{file}.txt", 'wt', encoding= "utf-8")
    new_text = input("Enter some text: ")
    file.write(new_text)
    return file.name

def open_create_read_and_check_file(file):
    file = create_file(file)
    file = open(f"{file}" , "rt", encoding= "utf-8")
    text =file.read()
    res = {}
    for sym in text:
        res[sym] = text.count(sym)
    
    print(res)

open_create_read_and_check_file(input("Write name file please: "))
    