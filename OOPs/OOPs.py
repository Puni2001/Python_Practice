# Class and Objects 

class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def startEngine(self):
        print(f"The {self.make} {self.model}'s engine is starting.")
        

toyotaCar = Car("Toyota", "camry", 2022)
toyotaCar.startEngine()
renaultcar = Car("Renault", "z-series", 2024)
renaultcar.startEngine()