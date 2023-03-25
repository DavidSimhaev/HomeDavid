"""3 сделайте так что пользователь вводит имя файла или "выход"
    если имя файла то в потоке считается количество слов и вводится на экран
    причем пока поток считает вы можете успеть ввести другое имя и запустить

    """


from home1 import MyOwnThread
while True:
    t = input("Enter filename: ")
    if t == "end":
        break
    try:
        with open(t, "r") as file:        
            p = MyOwnThread(t,1)
            p.start() 
    except Exception as ex:
        print(str(ex))
            