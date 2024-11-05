class Printer:
    manufacturer = "hp"
    count = 0
    
    def __init__(self, name = "OfficeJet Pro 8567e", speed = 35, price = 9500):
        self.__name = name
        self.__speed = speed
        self.__price = price
        Printer.count += 1
    
    def __del__(self):
        print("Printer " + self.__name + " is being deleted")
        Printer.count -= 1
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
    
    
    def __str__(self):
        return Printer.manufacturer + ": " + self.__name + " / " + str(self.__speed) + " ppm " + "(" + str(self.__price) + " грн" + ")"
    
    def __repr__(self):
        return f'Printer("{self.__name}", {self.__speed}, {self.__price})'
    


print(Printer.count)      
pr1 = Printer("OfficeJet Pro 8122e", 18, 7500)
# accessing class property using object
print(pr1.count) 
pr2 = Printer("OfficeJet Pro 8124e", 34, 19500)
print(Printer.count) 
pr3 = Printer("OfficeJet Pro 9720e", 24, 18000)
print(pr3.count) 
pr0 = Printer()
# method __str__ will be used (user friendly string)
print(pr0)
print(pr1)
print(pr2)
print(str(pr3))

print(repr(pr1))

del pr1
print(Printer.count)
del pr2
print(Printer.count)

print(pr3.get_name(), pr3.get_speed(), pr3.get_price(), sep=" ")


pr3.set_name("new name")
pr3.set_speed("15")
pr3.set_price("9000")
print(pr3)