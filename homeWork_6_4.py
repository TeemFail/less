print("""Урок 6 задача 4 - реализовать
	 класс Car, определить атрибуты name, 
	 speed, color, is_polise и методы go, 
	 stop, turn(direction). Описать 
	 дочерние классы TownCar, SportCar,
	  WorkCar, PoliseCar. Добавить метод 
	  show_speed, переопределить для 
	  WorkCar при 40 км и для TownCar при
	   60 выводить сообщение о превышении.
	    Создать экземпляры, передать данные,
	     проверить значения атрибутов и 
	     вызвать методы \n""")     
class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False
        
        
    def go(self):
        print(self.name)
        print("Начало движения \n")
                
       
    def stop(self):
        print(self.name)
        print("Остановка движения \n")
        
        
    def turn(self, direction):
        print(self.name)
        if direction == "right":
            print("Поворот направо \n")
        else:
            print("Поворот налево \n")
            
            
    def show_speed(self):
        print(self.name)
        print("Текущая скорость ", self.speed, "\n")
            
            
class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        
        
    def show_speed(self):
        print(self.name)   
        print("Текущая скорость ", self.speed, "\n")
        if self.speed >= 60:
            print("Превышение скорости \n")
    

class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)    
        

class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        
        
    def show_speed(self):
        print(self.name)
        print("Текущая скорость ", self.speed, "\n")
        if self.speed >= 40:
            print("Превышение скорости \n")


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        
        
volvo = TownCar("xc-90", 70, "red", False)
volvo.show_speed()

mb = SportCar("w222", 120, "green", False)
mb.go()
mb.turn("right")

truck = WorkCar("CAT", 50, "yelloy", False)
truck.show_speed()

policar = PoliceCar("police", 160, "red-white-blue", True)
policar.go()
policar.show_speed()


