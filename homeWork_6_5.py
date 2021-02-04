print("""Урок 6 задача 5 - реализовать
	класс Stationery, определить атрибут 
	title и методы draw. метод выводит
	сообщение -запуск отрисовки-. Создать
	дочерние классы Pen, Pensil, Handle
	для каждого класса переопределить
	метод, выводить уникальное сообщение
	создать экземпляры и проверить вывод \n""")     
class Stationery:
    def __init__(self, title):
        self.title = title
        
        
    def draw(self):
        print(self.title)
        print("Запуск отрисовки \n")
       
            
            
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        
        
    def draw(self):
        print(self.title)
        print("Запуск отрисовки для класса Pen \n")
    

class Pensil(Stationery):
    def __init__(self, title):
        super().__init__(title)
               
        
    def draw(self):
        print(self.title)
        print("Запуск отрисовки для класса Pensil\n")    
        

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        
        
    def draw(self):
        print(self.title)
        print("Запуск отрисовки для класса Handle \n")
        
        
tool_1 = Stationery("Просто кисть")
tool_1.draw()

tool_2 = Pen("Ручка")
tool_2.draw()

tool_3 = Pensil("Мягкий карандаш")
tool_3.draw()

tool_4 = Handle("Маркер")
tool_4.draw()

        


