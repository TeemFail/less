print("Урок 4 задача 5 - реализовать формирование списка через range используя генератор - только четные от 100 до 1000 включая границы. Получит результат произведения всех чисел, использовать reduce\n")
from functools import reduce

my_list=[]
for i in range(100,1002,2):
    my_list.append(i)
print("Исходный список: \n", my_list)
def my_funk(prev_el, el):
    return prev_el*el
    
    
print("\n Результат: \n",reduce(my_funk, my_list))