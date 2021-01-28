print("Урок 5 задача 5 - создать программно файл, записать программно числа через пробел и вывести их сумму  \n")
print("Файл для работы text5_5.txt \n")
with open ("text5_5.txt", "w") as my_text:
    my_text.write("23 1 7 89")
with open ("text5_5.txt") as my_text2:
    my_summ=sum(int (x) for x in my_text2.read().split())
print(my_summ)
