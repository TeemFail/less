print("""Урок 8 задача 6 - 
Продолжить работу над заданием. 
Реализуйте механизм валидации вводимых 
пользователем данных. Например, для 
указания количества принтеров, 
отправленных на склад, нельзя 
использовать строковый тип данных. \n""")

class Wahouse:
    def __init__(self):
        self._product={}
        
        
    def add_product(self, offequim):
        self._product.setdefault(offequim.name, []).append(offequim)
        
        
    def ext(self, name):
        if self._product[name]:
            self._product.setdefault(name).pop(0)
        
    

class OffEquim:
    def __init__(self, name, firm, model):
        self.name=name #printer, scanner, xerox
        self.firm=firm #samsung, epson etc
        self.model=model 
        #self.quantity=quantity
        #self.details=[]
        #self.technic={"Вид техники ":typ_tech, "производитель ":firm, "цена ":price, "количество ":quantity, "разное ":details}
        
        
        
    def __repr__(self):
        return f"{self.name} - {self.firm} - {self.model}"
        
        
        
        
class Printers(OffEquim):
    def __init__(self, name, firm, model, p_typ=None, p_color=None):
        super().__init__(name, firm, model)        
        self.p_typ=p_typ #laser, jet or niddles
        self.p_color=p_color #color or white_black
        
        
    @staticmethod   
    def tech_types(p_typ, p_color):
        model = (p_typ, p_color)
        return model
    
        
        
class Scanners(OffEquim):
    def __init__(self, name, firm, model):
        super().__init__(name, firm, model)
        #self.scan_typ=scan_typ #handle or planshet
        #self.scan_color=scan_color #color or white_black
        
        
        
    def tech_type(self):
        return "Planshet"
        
        
class Xerox(OffEquim):
    def __init__(self, name, firm, model):
        super().__init__(name, firm, model)
        #self.xer_typ=xer_typ #stationary or portable
        #self.xer_meth=xer_meth #analog, digital  
        
        
    def tech_types(self):
        return "Stationary"
        
        

wahouse = Wahouse()  
printer_new = Printers("printer", "HP", Printers.tech_types("laser", "color"))
wahouse.add_product(printer_new) 
printer_new = Printers("printer", "Samsung", "jet102")
wahouse.add_product(printer_new)
xerox_new = Xerox("xerox", "HP", "xtr23")
wahouse.add_product(xerox_new)
scaner_new = Scanners("scaner", "HP", "rf455")
wahouse.add_product(scaner_new)
print(wahouse._product, "\n")   
wahouse.ext("scaner")
print(wahouse._product)   