print("""Урок 7 задача 3 - 
реализовать программу работы с 
органическими клетками. Класс - клетка
в его конструкторе инициализировать 
параметр соответствующий количеству клеток
В классе должны быть реализованы
методы перезагрузки арифметических 
операторов: сложение, вычитание, деление
умножение. Данные методы должны применяться 
только к клеткам и именно их делить
складывать умножать и вычитать \n""")

class Cell:
    def __init__(self, cell):
        self.cell = cell
        
        
    def __add__(self, other):       
        return self.cell + other.cell
        
        
    def __sub__(self, other):
        return self.cell - other.cell
        
        
        
    def __mul__(self, other):
        return self.cell * other.cell
        
        
    def __tryediv__(self, other):
        return self.cell / other.cell
        
        
    def make_order(self, qty):
        cell_strok = ""
        cell_rem = self.cell
        for i in range(self.cell // qty):
            cell_strok += str("*" * qty + '\n')
        cell_strok += str("*" * (self.cell % qty))
        return cell_strok   
        
        
cell_1 = Cell(24)
cell_2 = Cell(8)

print(f'Клетка 1 = {cell_1.cell} в сумме с клеткой 2 = {cell_2.cell} дают клетку 3 = {cell_1.cell + cell_2.cell}\n')

print(f'Клетка 1 = {cell_1.cell} разность с клеткой 2 = {cell_2.cell} дают клетку 3 = {cell_1.cell - cell_2.cell}\n')

print(f'Клетка 1 = {cell_1.cell} умножить клеткой 2 = {cell_2.cell} дают клетку 3 = {cell_1.cell * cell_2.cell}\n')

print(f'Клетка 1 = {cell_1.cell} разделить клеткой 2 = {cell_2.cell} дают клетку 3 = {cell_1.cell // cell_2.cell}\n')

print(cell_1.make_order(5))