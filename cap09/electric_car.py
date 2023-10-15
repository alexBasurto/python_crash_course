from car import Car

class Battery:
    """Un simple intento de modelar una batería para un coche eléctrico."""

    def __init__(self, battery_size=75):
        """Inicializa los atributos de la batería."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Imprime una frase que describe el tamaño de la batería."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Imprime una frase sobre la autonomía que ofrece esta batería."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print (f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Representa aspectos de un coche propios de los vehículos eléctricos."""
    def __init__(self, make, model, year):
        """
        Inicializa los atributos de la clase base.
        Luego inicializa atributos propios de un coche eléctrico.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()