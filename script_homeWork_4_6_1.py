print("Урок 4 задача 6 - реализовать два скрипта - генератор с указанного числа и итератор повторяющий элементы некоторого списка определенного заранее, используя count и cycle \n")
from itertools import count
for el in count(int(input("Введите число "))):
    if el>10:
        	break
    else:
         print(el)