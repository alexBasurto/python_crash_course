#Modificar el valor de un atributo a través de un método.
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
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# my_new_car.odometter_reading = 50 #aquí probamos la resticción del método update_odometter

my_new_car.update_odometter(45)
my_new_car.read_odometter()