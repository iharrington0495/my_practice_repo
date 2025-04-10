class Car:
    def __int__(self, color, engine_type, gas_tank, odometer):
        self.color = color
        self.engine_type = engine_type
        self.gas_tank = gas_tank
        self.odometer = odometer

    def __str__(self):
        return f"{self.color} {self.engine_type}"
    
    def drive(self):
        if self.engine_type =="4_cylinder":
            if self.gas_tank >=3:
                self.gas_tank -= 3
                self.odometer += 90
            else:
                print("not enough fuel")
                
        elif self.engine_type == "V8":
             if self.gas_tank >=4:
                self.gas_tank -= 4
                self.odometer += 50

             else:
                print("not enough fuel")

    def get_gas_tank(self):
        return self.gas_tank
    
    def get_odometer(self):
        return self.odometer