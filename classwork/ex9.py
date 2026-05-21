class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year =  year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    @staticmethod
    def fill_gas_tank():
        print("Filling the gas tank...")

class Batterry():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car have {self.battery_size} -kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range_miles = 240
        elif self.battery_size == 85:
            range_miles = 270
        
        message = f"This car can go {range_miles}"
        print(message)

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("Battery upgraded to 85 kWh")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Batterry()


    @staticmethod
    def fill_gas_tank():
        print("This car dont need gas.")


my_tesla = ElectricCar("Tesla", "model s", 2020)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()