print("""Урок 7 задача 2 - 
Реализовать проект расчета суммарного
расхода ткани. Основной класс - одежда
к типам относится пальто и костюм. 
Параметры - размер для костюма и рост для
пальто (v / 6.5 + 0.5) (2 * h + 0.3)
соответственно. Реализовать подсчет 
общего расхода ткани, абстрактные классы
для основных классов, проверить на 
практике работу @property \n""")

from abc import ABC, abstractmethod
class Clothers(ABC):
    def __init__(self, V=None, H=None):
        self.V = V
        self.H = H
        
        
    @abstractmethod
    def consum(self):
        pass
        
        
          
class Costume(Clothers):
    def consum(self):
        return (self.V / 6.5 + 0.5)
            
            
class Coat(Clothers):
    def consum(self):
        return (2 * self.H + 0.3)
        
        
    @property
    def consum_gen(self):
        return (self.V / 6.5 + 0.5) + (2 * self.H + 0.3)
        
        
costume = Costume(V=20, H=30)
coat = Coat(H=30, V=20)
print("Расчет ткани на костюм и пальто: ", round(costume.consum(),2), "и",  round(coat.consum(), 2))

print("Расчет общего количества ткани: ",round(coat.consum_gen, 2))