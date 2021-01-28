print("Урок 5 задача 1 - создать программно текстовый файл, записать в него данные, вводимые пользователем, об окончании записи свидетельствует пустая строка \n")
with open ("text_my.txt", "w") as my_text:
    while True:
        my_line=input("Введите строку для записи в файл, окончание - пустая строка ")
        if len(my_line) == 0:
            break
        else:
            my_text.writelines(my_line+"\n")
