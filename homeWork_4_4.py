print("Урок 4 задача 4 - представлен список. Определить не имеющие повторений элементы, сформировать итоговый массив чисел, вывести в порядке их следования в списке, использовать генератор\n")
from random import randint
my_list=[]
for i in range(randint(0,20)): 
    my_list.append(randint(0,100))
print(my_list,"\n")
my_new_list=[el for el in my_list if my_list.count(el)==1]
print (my_new_list)