print("Представлен список. Вывести значения в другой список элементы, значения которых больше предыдущего элемента. Использовать генератор для формирования исходного списка\n")
from random import randint
rand_len_list=randint(5,15)
i=0
my_list=[]
while i <= rand_len_list:
    my_list.append(randint(0,300))
    i+=1
print(f"Исходный список \n{my_list}\n")
new_list=[my_list[i+1] for i in range(len(my_list)-1) if my_list[i+1]>my_list[i]]
print (f"Новый список \n{new_list}")