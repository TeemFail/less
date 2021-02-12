print("""Урок 8 задача 7 - 
Реализовать проект «Операции с 
комплексными числами». Создайте класс 
«Комплексное число», реализуйте 
перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу 
проекта, создав экземпляры класса 
(комплексные числа) и выполнив сложение
и умножение созданных экземпляров. 
Проверьте корректность полученного 
результата. \n""")

class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def __add__(self, other):
        self.sumzx = self.x + other.x
        self.sumzy = self.y + other.x
        
        
    def __mul__(self, other):
        self.mulx = self.x * other.x - self.y * other.y
        self.muly = self.x * other.x + self.x * other.y
        
        
x = float(input())
y = float(input())
a = ComplexNum(x, y)
x = float(input())
y = float(input())
b = ComplexNum(x, y)
a + b
a * b
print (f"Сумма: {a.sumzx} + {a.sumzy}\n")
print(f"Произведение: {a.mulx} + {a.muly}\n")







        
        
        

