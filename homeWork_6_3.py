print("Урок 6 задача 3 - реализовать класс Worker, определить атрибуты name, surname, position, income - защищенный и ссылается на словарь. Создать класс Position, реализовать методы получения имени и дохода. Создать экземпляры, передать данные, проверить значения атрибутов и вызвать методы \n")

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":5000, "bonus":2000}
        
       

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
        
        
    def get_full_name(self):
        print(self.name, self.surname)
                
       
    def get_total_income(self):
        print(self._income.get("wage")+self._income.get("bonus"))
        

Andrey = Position("Andrey", "Ivanov", "worker", {"wage":5000, "bonus":2000})
Andrey.get_full_name()
Andrey.get_total_income()

Vladimir = Position("Vladimir", "Smirnov", "worker", {"wage":6000, "bonus":3000})
Vladimir.get_full_name()
Vladimir.get_total_income()