print("""Урок 8 задача 4 - 
Начните работу над проектом « Склад 
оргтехники». Создайте класс, описывающий
склад. А также класс « Оргтехника», 
который будет базовым для классов-
наследников. Эти классы — конкретные 
типы оргтехники (принтер, сканер, 
ксерокс). В базовом классе определить 
параметры, общие для приведенных типов. 
В классах-наследниках реализовать 
параметры, уникальные для каждого типа 
оргтехники. \n""")

class Wahouse:
    def __init__(self):
        self.product=product
        
    

class OffEquim:
    def __init__(self):
        self.color=color #color of technics
        self.size=size #small, medium, large
        self.firm=firm #samsung, epson etc
        self.paper_size=paper_size #A4 etc
        self.resolution=resolution #high, medium or low
        
        
class Printers(OffEquim):
    def __init__(self):
        self.prin_typ=prin_typ #laser, jet or niddles
        self.prin_color=prin_color #color or white_black
        
        
class Scanners(OffEquim):
    def __init__(self):
        self.scan_typ=scan_typ #handle or planshet
        self.scan_color=scan_color #color or white_black
        
        
class Xerox(OffEquim):
    def __init__(self):
        self.xer_typ=xer_typ #stationary or portable
        self.xer_meth=xer_meth #analog, digital or color
    
    
            