print("""Урок 8 задача 2 - 
Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем 
нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не 
завершиться с ошибкой.\n""")

class DelZero(Exception):
    def __init__(self, txt):
        self.txt = txt
        

a = input("Введите делимое: \n")
b = input("Введите делитель: \n")     
try:          
    if int(b) == 0:
        raise DelZero("Делить на ноль нельзя!\n")          
except DelZero as err:
    print(err)
else:
    print(int(a) / int(b))
                
                                           
              