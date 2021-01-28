print("Урок 5 задача 3 - создать не программно текстовый файл, записать не менее 10 строк с фамилией и окладом, определить и вывести у кого оклад менее 20 тысяч. Выполнить подсчёт средней величины дохода \n")
print("Файл для работы ForHw5_3.txt \n")
my_money = 0
my_count = 0
with open ("ForHw5_3.txt", "r") as my_text:
    for line in my_text:
        my_line = line.split()
        my_money += int(my_line[1])
        my_count += 1
        if int(my_line[1]) <= 20000:
            print (" ".join(my_line))
print("\n Средняя величина дохода ", my_money/my_count)
            
       