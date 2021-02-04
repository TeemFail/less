print("Урок 6 задача 1 - создать класс светофор, определить атрибут цвет и метод запуск, режимы работы К-Ж-З посекундно 7-2-5, можно усложнить проверкой режимов  \n")
from time import sleep
class TrafficLight:
    __color = "color-blink_yellow"
    print("\nTrafficLight - work cycle\n")


    def tLmethRED(self):
        __color = "color-Red"
        print(__color)
        sleep(7)
        
        
    def tLmethYELLOW(self):
        __color = "color-Yellow"
        print(__color)
        sleep(2)
        
        
    def tLmethGREEN(self):
        __color = "color-Green"
        print(__color)
        sleep(5)
        
        
TL = TrafficLight()
while input("\n stop? - s \n") != "s":
    TL.tLmethRED()
    if TL._TrafficLight__color != "color-blink_yellow":
        print ("error cycle ")
    TL.tLmethYELLOW()
    if TL._TrafficLight__color != "color-blink_yellow":
        print ("error cycle ")
    TL.tLmethGREEN()