print("""Урок 8 задача 1 - 
Реализовать класс « Дата», функция
-конструктор которого должна принимать
дату в виде строки формата «день-месяц
-год». В рамках класса реализовать два
метода. Первый, с декоратором 
@classmethod, должен извлекать число, 
месяц, год и преобразовывать их тип к 
типу «Число». Второй, с декоратором  
@staticmethod, должен проводить 
валидацию числа, месяца и года 
(например, месяц — от 1 до 12). 
Проверить работу полученной структуры 
на реальных данных.  \n""")

class MDate:
    def __init__(self, my_date_str=None):
        self.my_date_str = my_date_str
        
        
    @classmethod
    def diass(cls, my_date_str):
        print("Через 'classmethod' \n", my_date_str, "\n")
        my_date = int(str(my_date_str).split("-")[0])
        print(my_date, "\n")
        my_month = int(str(my_date_str).split("-")[1])
        print(my_month, "\n")
        my_year = int(str(my_date_str).split("-")[2])
        print(my_year, "\n")
        
        
    @staticmethod
    def valid(my_date_str):
        print("Через 'staticmethod' \n", my_date_str, "\n")
        my_date = int(str(my_date_str).split("-")[0])
        if my_date < 1 or my_date > 31:
            print("Дата не валидна \n")
        my_month = int(str(my_date_str).split("-")[1])
        if my_month < 1 or my_month > 12:
            print("Месяц не валиден \n")
        my_year = int(str(my_date_str).split("-")[2])
        if my_year < 1 or my_year > 2021:
            print("Год не валиден \n")
    
        
    
MDate.diass("18-03-77")

MDate.valid("35-13-2050")

MDate.valid("12-11-99")
