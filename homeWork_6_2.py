print("Урок 6 задача 2 - создать класс дорога, определить атрибуты длина и ширина и метод расчета массы асфальта Д*Ш*Ма*Чи  \n")
class Road:
    def __init__(self, length, widht):
        self._length = length
        self._widht = widht


    def massa(self):
        massa1m = 25
        numberOfsm = 5
        return self._length*self._widht*massa1m*numberOfsm/1000



r = Road(20, 5000)
print(r.massa())
        
