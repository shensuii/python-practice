#9-9 BatteryUpgrade.py

class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_describe_name(self):
        return str(self.year) + " " + self.make + ' ' + self.model
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " mils on it")
        
    def updte_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odmeter!")
            
    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery. ")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print("This car can go approximately "+str(range)+".")

    def upgrade_battery(self):
        #升级电池容量
        if self.battery_size != 100:
            self.battery_size = 100
        print(self.battery_size)

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

ele_car=ElectricCar('tesla','model',2016)
ele_car.battery.get_range()
ele_car.battery.upgrade_battery()