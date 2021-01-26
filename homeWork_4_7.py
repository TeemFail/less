print("Урок 4 задача 7 - реализовать генератор с помощью функции используя yield. В цикле выводить числа от 1! до n!\n")
print("Через math-factorial\n")
from math import factorial
def generator_fact():
    n=int(input("Введите число: "))
    for el in range(1,n+1):
        yield factorial(el)
        
        
g=generator_fact()
for el in g:
    print (el)
print("\nЧерез функцию\n")
def fact(n):
    factorial=1
    for el in range(1,n+1):
        factorial*=el
        yield factorial
        	
        	
for i in fact(int(input("Введите число: "))):
    print(i)