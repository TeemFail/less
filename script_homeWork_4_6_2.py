print("Урок 4 задача 6 - реализовать два скрипта - генератор с указанного числа и итератор повторяющий элементы некоторого списка определенного заранее, используя count и cycle \n")
from itertools import cycle
stp=0 
for el in cycle("GeekBrains"):
    if stp>50:
        	break
    else:
         print(el)
         stp+=1