class Car:
    """Un simple intento de representar un coche."""

    def __init__(self, make, model, year):
        """Inicializa atributos para describir un coche."""
        self.make = make
        self.model = model
        self.year = year
        self.odometter_reading = 0

    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo con el formato adecuado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometter(self):
        """Imprime una oración que indica el kilometraje del coche."""
        print(f"This car has {self.odometter_reading} miles on it.")

    def update_odometter(self, mileage):
        """
        Configura el kilometraje con el valor dado.
        Rechaza el cambio si se intenta hacer retroceder el cuentakilómetros.
        """
        if mileage >= self.odometter_reading:
            self.odometter_reading = mileage
        else:
            print("You can't roll back an odometter.")

    def increment_odometter(self, miles):
        """
        Añade la cantidad dada a la lectura del cuentakilómetros.
        Rechaza el cambio si se intenta hacer retroceder el cuentakilómetros.
        """
        if miles >= 0:
            self.odometter_reading += miles
        else:
            print("You can't roll back an odometter.")

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
    
    def upgrade_battery(self):
        """Actualiza el valor de la batería cuando está cargada."""
        if self.battery_size <= 95:
            self.battery_size = 100

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

my_ford = ElectricCar('ford', 'kuga', 2023)
print(my_ford.get_descriptive_name())
my_ford.battery.describe_battery()
my_ford.battery.get_range()
my_ford.battery.upgrade_battery()
my_ford.battery.describe_battery()
my_ford.battery.get_range()